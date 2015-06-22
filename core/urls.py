from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',

                       url(r'^$', HomeView.as_view(), name='home'),

                       )
