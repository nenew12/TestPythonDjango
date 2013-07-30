from django.conf.urls import patterns, include, url
from pythonTestSite.view import hello, Fuck_you
 
urlpatterns = patterns('',
    url(r'^hello/$', hello),
    url(r'^FuckYou/$', Fuck_you),               
)
