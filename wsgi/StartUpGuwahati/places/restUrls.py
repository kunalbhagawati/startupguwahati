from django.conf.urls import patterns, url
from . import restViews

urlpatterns = patterns('',
    url(r'^$', restViews.PlacesList.as_view(), name='place-list'),
    url(r'^(?P<pk>[0-9]+)/',
        restViews.PlaceUpdate.as_view(),
        name='place-ops'),
)
