from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from core.views import *

admin.autodiscover()

urlpatterns = patterns('',
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'', include('core.urls', namespace='core')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
