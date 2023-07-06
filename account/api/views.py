from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User

from account.api.serializers import UserListSerializer,UserCreateSerilizer,UserUpdateSerilizer
from account.api.permissions import IsOwner

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerilizer

class UserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerilizer
    lookup_field = "pk"
    permission_classes = (IsOwner,)