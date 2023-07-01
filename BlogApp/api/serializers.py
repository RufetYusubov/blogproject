from rest_framework import serializers
from BlogApp.models import BlogModel,CategoryModel,TagCloudModel,CommentModel

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = "__all__"

class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        exclude = ("pub_date",)

    