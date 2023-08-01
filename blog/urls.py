from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from BlogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name="index"),
    path('blog/',include('BlogApp.urls')),
    path('account/',include('account.urls')),
    path('api-auth',include('rest_framework.urls')),
    path('api/',include("BlogApp.api.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS)
