from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^login/$', 'django.contrib.auth.views.login'),
    
    
    (r'^agenda/', include("session.urls")),
    (r'^profile/', include("account.urls")),
    (r'^register/?$', direct_to_template, {'template': 'register.html'}),
    (r'^fav/', include("fav.urls")),
    
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    ) + urlpatterns
