from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',
    (r'^add/(?P<session_id>\d+)/?$', 'dddm.fav.views.add'),
    (r'^del/(?P<session_id>\d+)/?$', 'dddm.fav.views.remove'),
)
