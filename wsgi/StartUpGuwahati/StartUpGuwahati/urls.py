from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import restViews, djangoViews

urlpatterns = patterns('',
    url(r'^api/', include(patterns('',
        url(r'^teapot/(?P<potType>[1234]{0,1})$',
                restViews.teapotView, name="teapot"),
        url(r'^twitterreader', include('twitterreader.restUrls')),
        url(r'^places', include('places.restUrls')),

        ),
    ), ), )

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('',
    url(r'^$', djangoViews.IndexView.as_view()),
    url(r'^twitterreader', include('twitterreader.djangoUrls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^foundation/', include('foundation.urls')),
)
