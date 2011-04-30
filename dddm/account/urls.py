from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',
    (r'^(?P<profile_id>\d+)/?$', 'dddm.account.views.person'),
)
