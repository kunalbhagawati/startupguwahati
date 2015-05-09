from django.conf.urls import patterns, include, url
from . import restViews

urlpatterns = patterns('',
    url(r'^$', restViews.PlacesList.as_view(), name='place-list'),

    url(r'^(?P<pk>[0-9]+)/', include(patterns('',
            url(r'^$',
                restViews.PlaceUpdate.as_view(),
                name='place-ops'),

            url(r'^images/$',
                restViews.PlaceImagesCreate.as_view(),
                name='place-images-create'),
        ), ), ),
)
