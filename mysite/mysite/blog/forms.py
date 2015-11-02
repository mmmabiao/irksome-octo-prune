from django import forms
from mysite.blog.models import *

__author__ = 'Administrator'


class BlogsPostForm(forms.ModelForm):
	class Meta:
		model = BlogsPost
		fields = ['title', 'body']


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment', ]
