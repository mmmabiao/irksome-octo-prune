from django.conf.urls import *

urlpatterns = patterns('mysite.blog.views',
    url(r'^$', 'index'),
    url(r'^/add/$', 'create_blog'),
    url(r'^/(?P<blog_id>[0-9]+)$', 'detail'),
)
