from django.conf.urls import patterns, include, url
from . import restViews

urlpatterns = patterns('',
    url(r'^$', restViews.PlaceList.as_view(), name='place-list'),
    url(r'^nearby/$', restViews.GetNearbyPlacesByLatLongView.as_view(),
        name='places-nearby'),

    url(r'^(?P<pk>[0-9]+)/', include(patterns('',
            url(r'^$',
                restViews.PlaceUpdate.as_view(),
                name='place-ops'),

            url(r'^images/$',
                restViews.PlaceImagesCreate.as_view(),
                name='place-images-create'),

            url(r'^images/(?P<imgId>[0-9]+)/$',
                restViews.PlaceImagesUpdate.as_view(),
                name='place-images-update'),
        ), ), ),
)
