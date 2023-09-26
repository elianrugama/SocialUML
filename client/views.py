from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from api.models import Posts, Comments, Likes, LikesComments, Historias, Mensajes
from django.http import JsonResponse
from django.contrib.auth.models import User

 

# Create your views here.
@login_required

def Home (request):
    posts = Posts.objects.all()
    posts = posts[::-1]
    historias = Historias.objects.all()
    historias = historias[::-1]
    mensajes = Mensajes.objects.all()
    mensajes = mensajes[::-1]
    users = User.objects.all()

    data = {
        'posts': posts,
        "historias": historias,
        "mensajes": mensajes,
        "users": users

    }
    return render(request, 'feed.html', data)

def Post(request):
    if request.method == 'POST':
        print(request.FILES)
        print(request.POST)
        image = request.FILES['image']
        title = request.POST['title']
        id_user = request.user


        post = Posts.objects.create(
            id_user = id_user,
            image = image,
            title = title,
            username = id_user.username,
        )
        post.save()
        return redirect('/')
    
    else:
        return redirect('/')