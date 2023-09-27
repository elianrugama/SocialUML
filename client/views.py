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
    return render(request, 'home.html', data)

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
    

def Perfil(request):
    posts = Posts.objects.filter(id_user = request.user)
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
    return render(request, 'perfil.html', data)
    



    
    
def Historia(request):
    if request.method == 'POST':
        print(request.FILES)
        print(request.POST)
        image = request.FILES['image']
        id_user = request.user
        
        historia = Historias.objects.create(
            id_user = id_user,
            image = image,
            username = id_user.username,
        )
        historia.save()
        return redirect('/')
    
    else:
        return redirect('/')
    

def Chat(request, id_user):
    if request.method == 'POST':
        print(request.POST)
        print(request.user)
        print(id_user)
        id_user2 = User.objects.get(id=id_user)
        id_user = request.user
        message = request.POST['bodyMensaje']

        mensaje = Mensajes.objects.create(
            id_user = id_user,
            id_user2 = id_user2,
            body = message,
            username = id_user.username,
        )
        mensaje.save()
        return redirect('/chats/' + str(id_user2.id))
    id_userN = User.objects.get(id=id_user)
    
    posts = Posts.objects.all()
    posts = posts[::-1]
    historias = Historias.objects.all()
    historias = historias[::-1]

    # Obtener los mensajes del usuario actual y del receptor
    mensajes_usuario = list(Mensajes.objects.filter(id_user=request.user, id_user2=id_userN))
    mensajes_receptor = list(Mensajes.objects.filter(id_user=id_userN, id_user2=request.user))

    # Combinar los mensajes intercaladamente
    mensajes_combinados = []
    total_mensajes = max(len(mensajes_usuario), len(mensajes_receptor))

    for i in range(total_mensajes):
        if i < len(mensajes_usuario):
            mensajes_combinados.append(mensajes_usuario[i])

        if i < len(mensajes_receptor):
            mensajes_combinados.append(mensajes_receptor[i])

    print(mensajes_combinados)

    users = User.objects.all()
    user = User.objects.get(id=id_user)

    data = {
        'posts': posts,
        'historias': historias,
        'mensajes': mensajes_combinados,
        'users': users,
        'user': user
    }
    return render(request, 'chat.html', data)

def Chats(request):
    posts = Posts.objects.all()
    posts = posts[::-1]
    historias = Historias.objects.all()
    historias = historias[::-1]

    # Obtener los mensajes del usuario actual y del receptor
    mensajes_usuario = list(Mensajes.objects.filter(id_user=request.user))
    mensajes_receptor = list(Mensajes.objects.filter(id_user2=request.user))

    # Combinar los mensajes intercaladamente
    mensajes_combinados = []
    total_mensajes = max(len(mensajes_usuario), len(mensajes_receptor))

    for i in range(total_mensajes):
        if i < len(mensajes_usuario):
            mensajes_combinados.append(mensajes_usuario[i])

        if i < len(mensajes_receptor):
            mensajes_combinados.append(mensajes_receptor[i])

    print(mensajes_combinados)
    ultimos_mensajes = []

    for mensaje in mensajes_combinados:
        if mensaje.id_user == request.user:
            if mensaje.id_user2 not in ultimos_mensajes:
                ultimos_mensajes.append(mensaje.id_user2)
        else:
            if mensaje.id_user not in ultimos_mensajes:
                ultimos_mensajes.append(mensaje.id_user)

    users = User.objects.all()

    data = {
        'posts': posts,
        'historias': historias,
        'mensajes': ultimos_mensajes,
        'users': users
    }
    return render(request, 'chats.html', data)


def Eliminarcomentarios(request, id):
    comentario = Comments.objects.get(id=id)
    comentario.delete()
    return JsonResponse({'status': 'ok'})