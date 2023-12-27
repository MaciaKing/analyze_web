from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('virus_total', views.prueba_vt, name='prueba_vt'),
]