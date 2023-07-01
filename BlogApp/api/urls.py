from django.urls import path
from BlogApp.api import views

urlpatterns = [
    path('list-create/',views.BlogListCreateAPIView.as_view(),name="list-create"),
    path("retrieve-update-delete/<int:id>/",views.BlogRetrieveUpdateDestroyAPIView.as_view(),name="retrieve-update-delete"),
    
]