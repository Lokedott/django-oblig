from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import patterns, url


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")




from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)


urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)