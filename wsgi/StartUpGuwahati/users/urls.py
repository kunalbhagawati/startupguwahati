from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', restViews.UserList.as_view(), name='user-list'),

    url(r'^(?P<pk>[0-9]+)/', include(patterns('',
            url(r'^$',
                restViews.UserUpdate.as_view(),
                name='user-ops'),
        ), ), ),
)
