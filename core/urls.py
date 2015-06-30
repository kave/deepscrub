from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='home'),
                       url(r'^details/(?P<pk>\d+)$', product_detail_view, name='product_details'),
                       )
