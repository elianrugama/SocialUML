from django.urls import include, path
from . import views

urlpatterns = [
        path('accounts/', include('django.contrib.auth.urls')),
        path('logout/', views.logout, name='logout'),
        path('register/', views.register, name='register'),
        path('codigo/<str:codigo>/', views.codigo, name='codigo'),

]
