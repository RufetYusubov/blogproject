from django.urls import path
from BlogApp import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name="home"),
    path('category/<int:id>',views.CategoryView.as_view(),name="categorylink")
]