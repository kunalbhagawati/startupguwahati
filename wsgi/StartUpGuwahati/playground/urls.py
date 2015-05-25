from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^(?P<pk>[0-9]+)/', include(patterns('',
        url(r'^$',
            views.GetUpdateDeleteDummyView.as_view(), name="noauth-instance"),
        url(r'^basic$',
            views.BasicAuthGetUpdateDeleteDummyView.as_view(),
            name="basicauth-instance"),
        # url(r'^basic/', views.teapotView, name="basic-list"),
        ), ), ),

    url(r'^', include(patterns('',
        url(r'^$',
            views.DummyList.as_view(), name="noauth-list"),
        url(r'^basic$',
            views.BasicAuthDummyList.as_view(), name="noauth-list"),

        # url(r'^basic/', views.DummyList, name="basic-list"),
        ), ), ),
    )
