from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view()),
    url(r'^teapot/(?P<potType>[1234]{0,1})$', views.teapotView, name="teapot"),
    url(r'^admin/', include(admin.site.urls)),
)
