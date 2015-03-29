from django.conf.urls import patterns, include, url
from . import restViews

urlpatterns = patterns('',
    url(r'^$', restViews.FetchResults.as_view()),
)
