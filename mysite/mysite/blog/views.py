import django.template
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from mysite.blog.models import BlogsPost
from .forms import BlogsPostForm
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.


def index(request):
	posts = BlogsPost.objects.all()
	t = django.template.loader.get_template("index.html")
	c = django.template.Context({'posts': posts})
	return HttpResponse(t.render(c))


@login_required(login_url='/online/login/')
def create_blog(request):
	if request.method == 'POST':
		form = BlogsPostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			body = form.cleaned_data['body']
			timestamp = form.cleaned_data['timestamp']
			BlogsPost.objects.create(title=title, body=body, timestamp=timestamp)
			return HttpResponse('create blog success!!')
	else:
		form = BlogsPostForm()
	return render_to_response('create_blog.html', {'form': form}, context_instance=RequestContext(request))


def detail(request, pk):
	blog = BlogsPost.objects.get(id=pk)
	return HttpResponse('')
