from django.db import models
from django.contrib import admin


# Create your models here.
class BlogsPost(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateTimeField()
	user = models.CharField(max_length=150)


class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'timestamp')

	class Meta:
		ordering = ('-timestamp',)


class Comment(models.Model):
	comment = models.TextField()
	bid = models.IntegerField()
# uid = models.ForeignKey(User)


admin.site.register(BlogsPost, BlogPostAdmin)
