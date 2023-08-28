from django.shortcuts import render
from rest_framework import viewsets
from .models import Posts, Comments, Likes
from .serializers import PostsSerializer, CommentsSerializer, LikesSerializer

# Create your views here.

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

    