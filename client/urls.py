from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.Home, name='home'),
    path('perfil/', views.Perfil, name='perfil'),
   
    path('post/', views.Post, name='post'),
    path('historias/', views.Historia, name='historia'),
    path('chats/', views.Chats, name='chats'),
    path('chats/<int:id_user>/', views.Chat, name='chat'),
    path('eliminarcomentarios/<int:id>', views.Eliminarcomentarios, name='eliminarcomentarios'),
    path('grupos/', views.Home, name='home'),
    path('paginas/', views.Home, name='home'),
    path('eventos/', views.Home, name='home'),

    


]