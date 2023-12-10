from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('accounts/create/', views.create, name='create'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home')
]