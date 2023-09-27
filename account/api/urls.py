from django.urls import path
from account.api import views

urlpatterns = [
    path('user-list/', views.UserListAPIView.as_view()),
    path('user-create/',views.UserCreateAPIView.as_view()),
    path('user-retrieve-update-delete/<int:pk>/',views.RetrieveUpdateDestroyAPIView.as_view()), 
]