from rest_framework.generics import (
    ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView,
    RetrieveUpdateDestroyAPIView,ListCreateAPIView
)

from rest_framework.permissions import IsAdminUser,IsAuthenticated
                                     
from BlogApp.models import BlogModel, CategoryModel,TagCloudModel,CommentModel
from BlogApp.api.serializers import BlogSerializer,CategorySerializer,TagCloudSerializer,CommentSerializer

from BlogApp.api.permissions import IsOwner

class BlogListAPIView(ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class BlogCreateAPIView(CreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)



class BlogRetrieveAPIView(RetrieveAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"

class BlogUpdateAPIView(UpdateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"
    permission_classes = (IsOwner,)


class BlogDestroyAPIView(DestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"
    permission_classes = (IsOwner,)
#-----------------------------------------------------------------------------------------
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"

#-----------------------------------------------------------------------------------------

class TagListCreateAPIView(ListCreateAPIView):
    queryset = TagCloudModel
    serializer_class = TagCloudSerializer

class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TagCloudModel
    serializer_class = TagCloudSerializer
    lookup_field = "id"

#---------------------------------------------------------------------------------------

class CommentListCreateAPIView(ListCreateAPIView):
    queryset = CommentModel
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CommentModel
    serializer_class = CommentSerializer
    lookup_field = "id"




    



