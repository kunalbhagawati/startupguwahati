from django.conf import settings
from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^/', include(patterns('',
        url(r'^basic/',
                views.teapotView, name="teapot"),
        # url(r'^twitterreader', include('twitterreader.restUrls')),
        url(r'^places/', include('places.restUrls')),
        url(r'^users/', include('users.restUrls')),
        url(r'^playground/', include('playground.urls')),
        ),
    ), ), )
