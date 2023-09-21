from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from api.models import Posts, Comments, Likes
from django.http import JsonResponse

 

# Create your views here.
@login_required


def Home (request):
    posts = Posts.objects.all()
    posts = posts[::-1]
    data = {
        'posts': posts
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
            title = title
        )
        post.save()
        return redirect('/')
    
    else:
        return redirect('/')