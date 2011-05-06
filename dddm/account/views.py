from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from lazysignup.utils import is_lazy_user
from lazysignup.forms import UserCreationForm
from lazysignup.decorators import allow_lazy_user
from lazysignup.exceptions import NotLazyError
from lazysignup.forms import UserCreationForm
from lazysignup.models import LazyUser

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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


@allow_lazy_user
def convert(request, form_class=UserCreationForm, anonymous_redirect="/"):
    """ Convert a temporary user to a real one. Reject users who don't
    appear to be temporary users (ie. they have a usable password)
    """

    # If we've got an anonymous user, redirect to login
    if request.user.is_anonymous():
        return HttpResponseRedirect(anonymous_redirect)

    if request.method == 'POST':
        redirect_to = "/agenda/"
        form = form_class(request.POST, instance=request.user)
        if form.is_valid():
            try:
                user = LazyUser.objects.convert(form)
            except NotLazyError:
                return redirect(redirect_to)

            # Re-log the user in, as they'll now not be authenticatable with the Lazy
            # backend
            login(request, authenticate(**form.get_credentials()))
            
            request.user.first_name = request.POST["first_name"]
            request.user.last_name = request.POST["last_name"]
            request.user.save()
            
            redirect(redirect_to)
    else:
        form = form_class()
    
    return redirect("/")