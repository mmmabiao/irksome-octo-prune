import django.template
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from mysite.blog.models import BlogsPost, Comment
from .forms import BlogsPostForm, CommentForm
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.


def index(request):
	posts = BlogsPost.objects.all()
	return render_to_response('index.html', {'posts': posts}, context_instance=RequestContext(request))


# @login_required(login_url='/online/login/')
def create_blog(request):
	if request.method == 'POST':
		form = BlogsPostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			body = form.cleaned_data['body']
			BlogsPost.objects.create(title=title, body=body, )
			return index(request)
	else:
		form = BlogsPostForm()
	return render_to_response('create_blog.html', {'form': form}, context_instance=RequestContext(request))


def detail(request, pk):
	blog = BlogsPost.objects.get(id=pk)
	mm = Comment.objects.all()
	return render_to_response('detail.html', {'blog': blog, 'mm': mm}, context_instance=RequestContext(request))


def comment(request, pk):
	s = BlogsPost.objects.get(id=pk)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			a = form.cleaned_data['comment']
			Comment.objects.create(comment=a, bid=s.id,)
			return detail(request, s.id)
	else:
		form = CommentForm()
	return render_to_response('comments.html', {'form': form}, context_instance=RequestContext(request))
