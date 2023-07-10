from django.urls import path
from BlogApp import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name="index"),
    path('category/<int:id>/',views.CategoryView.as_view(),name="categorylink"),
    path('tagcloud/<int:id>/',views.TagCloudView.as_view(),name="tagcloud"),
    path('detail/<int:id>',views.PostDetailView.as_view(),name="post-details"),
    path('about/',views.AboutView.as_view(),name="about"),
]