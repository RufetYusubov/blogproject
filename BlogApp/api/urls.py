from django.urls import path
from BlogApp.api import views

urlpatterns = [
    path('list-create/',views.BlogListCreateAPIView.as_view(),name="list-create"),
    path("retrieve-update-delete/<int:id>/",views.BlogRetrieveUpdateDestroyAPIView.as_view(),name="retrieve-update-delete"),

    path('category-list-create/',views.CategoryListCreateAPIView.as_view()),
    path('category-retrieve-update-delete/<int:id>/',views.CategoryRetrieveUpdateDestroyAPIView.as_view()),

    path('tag-list-create/',views.TagListCreateAPIView.as_view()),
    path('tag-retrieve-update-delete/<int:id>/',views.TagRetrieveUpdateDestroyAPIView.as_view()),

    path('comment-list-create/',views.CommentListCreateAPIView.as_view()),
    path('comment-retrieve-update-delete/<int:id/',views.CommentRetrieveUpdateDestroyAPIView.as_view())
]