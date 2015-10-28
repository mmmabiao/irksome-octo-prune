from django.template import loader,Context
from django.http import HttpResponse

from mysite.blog.models import BlogsPost


# Create your views here.


def index(request):
    posts = BlogsPost.objects.all()
    t = loader.get_template("index.html")
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))


def create_blog(request):
    return HttpResponse('')


def detail(request, blog_id):
    return HttpResponse('')
