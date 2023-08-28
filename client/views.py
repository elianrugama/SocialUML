from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.models import Posts, Comments, Likes

 

# Create your views here.
@login_required


def Home (request):
    posts = Posts.objects.all()
    data = {
        'posts': posts
    }
    return render(request, 'feed.html', data)
