from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404

# Custom models
from dddm.fav.models import Fav
from dddm.session.models import Session


def add(request, session_id):
    """
    Favourite a session
    """

    session = get_object_or_404(Session, pk=session_id)
    if session.is_break:
        raise Http404
    
    f = Fav.objects.filter(user=request.user).filter(session=session)
    
    if not f.exists():
        Fav.objects.create(user=request.user, session=session)
    
    n = Fav.objects.filter(user=request.user).filter(session__slot=session.slot).count()
    if n > 1:
        clash = Fav.objects.filter(user=request.user)\
                           .filter(session__slot=session.slot)\
                           .exclude(session=session)
    else:
        clash = None

    return render_to_response('new_fav.html',
                             {"session": session,
                              "clash": clash},
                             context_instance=RequestContext(request))

def remove(request, session_id):
    """
    Remove a favourite :(
    """

    session = get_object_or_404(Session, pk=session_id)
    if session.is_break:
        raise Http404
    
    f = Fav.objects.filter(user=request.user).filter(session=session)
    if f.exists():
        f.delete()

    return render_to_response('del_fav.html',
                             {"session": session},
                             context_instance=RequestContext(request))
