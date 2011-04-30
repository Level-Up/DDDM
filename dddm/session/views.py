from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404
from lazysignup.decorators import allow_lazy_user

# Custom models
from dddm.fav.models import Fav
from dddm.session.models import Session

@allow_lazy_user
def detail(request, slug):
    """
    Show a single session
    """

    session = get_object_or_404(Session, slug=slug)
    if session.is_break:
        raise Http404

    return render_to_response('session.html',
                             {"session": session},
                             context_instance=RequestContext(request))
