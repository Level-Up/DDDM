from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from lazysignup.decorators import allow_lazy_user
from lazysignup.utils import is_lazy_user

# Custom models
from dddm.fav.models import Fav
from dddm.session.models import Session


@allow_lazy_user
def person(request, profile_id):
    """
    Show one of the awesome speakers or attendees
    """

    requested_user = get_object_or_404(User, pk=profile_id)
    if is_lazy_user(requested_user):
        raise Http404
    
    qs = Fav.objects.filter(user=requested_user)
    attending = [x.session for x in qs] if qs.exists() else None

    return render_to_response('profile.html',
                             {"person": requested_user,
                              "attending": attending},
                             context_instance=RequestContext(request))
