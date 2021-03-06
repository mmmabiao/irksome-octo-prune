from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


# Create your models here.
class BlogsPost(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateTimeField(auto_now=True)
	# user = models.ForeignKey(User, null=True)


class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'timestamp')

	class Meta:
		ordering = ('-timestamp',)


class Comment(models.Model):
	comment = models.TextField()
	bid = models.IntegerField()
	ctime = models.DateTimeField(auto_now=True, null=True)
	# user = models.ForeignKey(User, null=True)


# uid = models.ForeignKey(User)


admin.site.register(BlogsPost, BlogPostAdmin, )
