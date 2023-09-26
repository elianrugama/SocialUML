from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.Home, name='home'),
    path('perfil/', views.Perfil, name='perfil'),
   
    path('post/', views.Post, name='post'),
    


]