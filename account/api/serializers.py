from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)



class UserCreateSerilizer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username","password")

class UserUpdateSerilizer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"