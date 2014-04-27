from django.conf.urls import patterns, include, url
from agiliq_oauth import views

urlpatterns = patterns('',
    # Examples:
    url(r'^agiliq_oauth$', views.agiliq_oauth,name = "agiliq_oauth"),
    url(r'^response/$', views.agiliq_response,name = "agiliq_response"),

)
