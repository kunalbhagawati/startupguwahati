from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^(?P<pk>[0-9]+)/', include(patterns('',
        url(r'^$',
            views.GetUpdateDeleteDummyView.as_view(), name="noauth-instance"),
        url(r'^basic$',
            views.BasicAuthGetUpdateDeleteDummyView.as_view(),
            name="basicauth-instance"),
        url(r'^session$',
            views.SessionAuthGetUpdateDeleteDummyView.as_view(),
            name="sessionauth-instance"),
        url(r'^token$',
            views.TokenAuthGetUpdateDeleteDummyView.as_view(),
            name="tokenauth-instance"),
        ), ), ),

    url(r'^', include(patterns('',
        url(r'^$',
            views.DummyList.as_view(), name="noauth-list"),
        url(r'^basic$',
            views.BasicAuthDummyList.as_view(), name="basicauth-list"),
        url(r'^session$',
            views.SessionAuthDummyList.as_view(), name="sessionauth-list"),
        url(r'^token$',
            views.TokenAuthDummyList.as_view(), name="tokenauth-list"),
        ), ), ),
    )
