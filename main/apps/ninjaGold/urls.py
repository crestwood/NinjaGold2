from django.conf.urls import url
from . import views           # This line is new!This explicitly imports views.py in the current folder.
urlpatterns = [
    url(r'^$', views.index),
    url(r'^processMoney', views.processMoney),
    # url(r'^create$', views.create),
    # url(r'^displayName$', views.displayName),
    # url(r'^(?P<number>\d+)$', views.show),
    # url(r'^(?P<number>\d+)/edit$', views.edit),
    # url(r'^(?P<number>\d+)/delete$', views.destroy)
    
         # This line has changed! Notice that urlpatterns is a list, the comma is in
] 