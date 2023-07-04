from django.contrib import admin
from BlogApp.models import BlogModel,CategoryModel,TagCloudModel,CommentModel,AboutModel

admin.site.register(BlogModel)
admin.site.register(CategoryModel)
admin.site.register(TagCloudModel)
admin.site.register(CommentModel)
admin.site.register(AboutModel)