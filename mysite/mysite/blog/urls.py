from django.conf.urls import *
import views

urlpatterns = patterns('mysite.blog.views',
					   url(r'^$', 'index'),
					   url(r'^(?P<pk>[0-9]+)/$', views.detail), )
