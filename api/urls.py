from django.urls import include, path
from rest_framework import routers
from .views import PostsViewSet, CommentsViewSet, LikesViewSet

router = routers.DefaultRouter()
router.register('posts', PostsViewSet)
router.register('comments', CommentsViewSet)
router.register('likes', LikesViewSet)

urlpatterns= [
    path('api/', include(router.urls))

]
