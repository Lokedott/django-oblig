from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import patterns, url


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")




from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)