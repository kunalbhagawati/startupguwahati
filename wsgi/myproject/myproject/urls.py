from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import restViews, djangoViews

urlpatterns = patterns('',
    url(r'^api/', include(patterns('',
        url(r'^teapot/(?P<potType>[1234]{0,1})$', 
            restViews.teapotView, name="teapot"),
        )))
)

urlpatterns += patterns('',
    url(r'^$', djangoViews.IndexView.as_view()),
    url(r'^callback', djangoViews.TWCallbackView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
