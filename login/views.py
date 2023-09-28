from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Codigo
from django.contrib.auth.models import User

# Create your views here.
def logout (request):
    request.session.clear()
    return redirect('/')

def register (request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        usuario = request.POST['username']
        contraseña = request.POST['contraseña']
        email = request.POST['email']

        if Codigo.objects.filter(codigo=codigo).exists():
            return JsonResponse({'error': 'El codigo ya existe'})
        else:
            nuevoCodigo = Codigo(codigo=codigo, usuario=usuario, contraseña=contraseña)
            nuevoCodigo.save()
            nuevoUsuario = User.objects.create_user(username=usuario, password=contraseña, email=email)
            nuevoUsuario.save()
            return JsonResponse({'success': 'El codigo se ha registrado correctamente', "usuario": usuario, "contraseña": contraseña})
        
    else:
        return redirect('/')
    

def codigo (request, codigo):
    if Codigo.objects.filter(codigo=codigo).exists():
        codigo = Codigo.objects.get(codigo=codigo)
        return JsonResponse({'success': 'El codigo existe', "usuario": codigo.usuario, "contraseña": codigo.contraseña})
    else:
        return JsonResponse({'error': 'El codigo no existe'})
    

