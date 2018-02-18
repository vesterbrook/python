from django.conf.urls import url, include
from . import views
urlpatterns = [

    url(r'^$', views.index),     # This line has changed!
    url(r'^rando$', views.rando),
    url(r'^reset$', views.reset)
]