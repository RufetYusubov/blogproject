from django.urls import path
from BlogApp.api import views

urlpatterns = [
    path('blog-list/',views.BlogListAPIView.as_view(),name="blog-list"),
    path('blog-create/',views.BlogCreateAPIView.as_view(),name="blog-create"),
    path("blog-retrieve/<int:id>/",views.BlogRetrieveAPIView.as_view(),name="blog-retrieve"),
    path("blog-update/<int:id>/",views.BlogUpdateAPIView.as_view(),name="blog-update"),
    path("blog-delete/<int:id>/",views.BlogDestroyAPIView.as_view(),name="blog-delete"),

    path('category-list-create/',views.CategoryListCreateAPIView.as_view()),
    path('category-retrieve-update-delete/<int:id>/',views.CategoryRetrieveUpdateDestroyAPIView.as_view()),

    path('tag-list-create/',views.TagListCreateAPIView.as_view()),
    path('tag-retrieve-update-delete/<int:id>/',views.TagRetrieveUpdateDestroyAPIView.as_view()),

    path('comment-list-create/',views.CommentListCreateAPIView.as_view()),
    path('comment-retrieve-update-delete/<int:id>/',views.CommentRetrieveUpdateDestroyAPIView.as_view())
]