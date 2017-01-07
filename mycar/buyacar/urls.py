from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^time/$', views.currenttime, name='currenttime'),
    url(r'^test/$', views.testtemplate, name='testtemplate'),
]