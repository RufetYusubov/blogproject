from rest_framework.generics import (
    ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView,
    RetrieveUpdateDestroyAPIView,ListCreateAPIView
)
                                     
from BlogApp.models import BlogModel
from BlogApp.api.serializers import BlogSerializer,BlogCreateSerializer

class BlogListCreateAPIView(ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class BlogRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"




    



