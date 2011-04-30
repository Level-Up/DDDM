from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',
    (r'(?P<slug>[-\w]+)/?$','dddm.session.views.detail'),
)
