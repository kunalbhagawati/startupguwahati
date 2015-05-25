from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^/', include(patterns('',
        url(r'^$', views.DummyList, name="noauth-list"),
        # url(r'^basic/', views.DummyList, name="basic-list"),
        ), ), ),

    url(r'^/(?P<pk>[0-9]+)/', include(patterns('',
        url(r'^$', views.GetUpdateDeleteDummyView, name="noauth-instance"),
        # url(r'^basic/', views.teapotView, name="basic-list"),
        ), ), ),
    )
