from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404
from lazysignup.decorators import allow_lazy_user
from lazysignup.utils import is_lazy_user

# Custom models
from dddm.fav.models import Fav
from dddm.session.models import Session


@allow_lazy_user
def detail(request, slug):
    """
    Show a single session, with attendees
    """

    session = get_object_or_404(Session, slug=slug)
    if session.is_break:
        raise Http404

    qs = Fav.objects.filter(session=session)
    attendees = [x.user for x in qs if not is_lazy_user(x.user)] if qs.exists() else None

    return render_to_response('session.html',
                             {"session": session,
                              "attendees":attendees},
                             context_instance=RequestContext(request))
