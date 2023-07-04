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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"

class TagCloudSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagCloudModel
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        modal = CommentModel
        fields = "__all__"

    