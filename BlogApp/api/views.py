from rest_framework.generics import (
    ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView,
    RetrieveUpdateDestroyAPIView,ListCreateAPIView
)
                                     
from BlogApp.models import BlogModel, CategoryModel,TagCloudModel,CommentModel
from BlogApp.api.serializers import BlogSerializer,CategorySerializer,TagCloudSerializer,CommentSerializer

class BlogListCreateAPIView(ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class BlogRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"

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




    



