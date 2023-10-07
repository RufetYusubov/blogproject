from django.urls import path
from account import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(),name="signup"),
    path('login/', views.LoginView.as_view(),name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('changepassword/',views.ChangepasswordView.as_view(),name="changepassword"),
    path('contact/',views.ContactView.as_view(),name="contact")   
]
