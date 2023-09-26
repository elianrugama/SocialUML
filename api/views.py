from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Posts, Comments, Likes
from .serializers import PostsSerializer, CommentsSerializer, LikesSerializer
from django.http import JsonResponse
# Create your views here.
#evitar el csrf token
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

def Comentarios(request, id_post):
    comments = Comments.objects.filter(id_post=id_post).values()
    comments = comments[::-1]
    
    comments = list(comments)
    print(comments)
    return JsonResponse(comments, safe=False)



@csrf_exempt
def Comentar(request):
    if request.method == 'POST':
        print(request.POST)
        
        id_post = request.POST['id_post']
        body = request.POST['body']
        id_user = request.user
        username = id_user.username

        comment = Comments.objects.create(
            id_post = Posts.objects.get(id=id_post),
            id_user = id_user,
            body = body,
            username = username
        )
        comment.save()
        return JsonResponse({'status': 'success'})
    else:
        return redirect('/')
    