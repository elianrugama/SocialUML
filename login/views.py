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
        usuario = request.POST['email']
        contraseña = request.POST['contraseña']
        if Codigo.objects.filter(codigo=codigo).exists():
            return JsonResponse({'error': 'El codigo ya existe'})
        else:
            nuevoCodigo = Codigo(codigo=codigo, usuario=usuario, contraseña=contraseña)
            nuevoCodigo.save()
            nuevoUsuario = User.objects.create_user(username=usuario, password=contraseña)
            nuevoUsuario.save()
            return JsonResponse({'success': 'El codigo se ha registrado correctamente'})
        
    else:
        return redirect('/')