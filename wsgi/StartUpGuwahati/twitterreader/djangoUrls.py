from django.conf.urls import patterns, include, url
from . import djangoViews

urlpatterns = patterns('',
    url(r'^$', djangoViews.IndexView.as_view()),
)