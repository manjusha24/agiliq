from django.conf.urls import patterns, include, url
from agiliq_oauth import views, agiliq_views

urlpatterns = patterns('',
    # Examples:
    url(r'^agiliq_oauth$', agiliq_views.agiliq_oauth,name = "agiliq_oauth"),
    url(r'^response/$', agiliq_views.agiliq_response,name = "agiliq_response"),

)