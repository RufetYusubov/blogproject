from django.contrib import admin
from BlogApp.models import BlogModel,CategoryModel,TagCloudModel,CommentModel

admin.site.register(BlogModel)
admin.site.register(CategoryModel)
admin.site.register(TagCloudModel)