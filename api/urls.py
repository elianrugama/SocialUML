from django.urls import include, path
from rest_framework import routers
from .views import PostsViewSet, CommentsViewSet, LikesViewSet, Comentarios, Comentar

router = routers.DefaultRouter()
router.register('posts', PostsViewSet)
router.register('comments', CommentsViewSet)
router.register('likes', LikesViewSet)

urlpatterns= [
    path('api/', include(router.urls)),
    path('api/comentarios/<int:id_post>/', Comentarios, name='comentarios'),
    path('api/comentar/', Comentar, name='comentar'),
    

    

]
