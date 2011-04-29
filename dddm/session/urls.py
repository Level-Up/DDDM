from django.conf.urls.defaults import *
from django.conf import settings
from dddm.session.models import Session


session_detail_dict = {'queryset': Session.objects.all(),
                       'template_name': 'session.html',
                       'template_object_name': 'session',
                       'slug_field': 'slug'}

urlpatterns = patterns('',
    (r'(?P<slug>[-\w]+)/?$','django.views.generic.list_detail.object_detail', session_detail_dict),
)
