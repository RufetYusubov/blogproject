from django.urls import path
from BlogApp import views

urlpatterns = [
    path('category/<int:id>/',views.CategoryView.as_view(),name="categorylink"),
    path('tagcloud/<int:id>/',views.TagCloudView.as_view(),name="tagcloud"),
    path('blogentrie/',views.BlogView.as_view(),name = "blog" ),
    path('detail/<int:id>/',views.PostDetailView.as_view(),name="post-details"),
    path('search/', views.search_view, name='search_view'),
    path('delete/<int:id>/',views.DeleteComment,name="delete_comment"),
    path('about/',views.AboutView.as_view(),name="about"),
]