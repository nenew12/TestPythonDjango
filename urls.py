from django.conf.urls import patterns, include, url
from pythonTestSite.view import hello
 
urlpatterns = patterns('',
    url(r'^hello/$', hello),               
)