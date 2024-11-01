from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuario.forms import FormularioDeRegistroDeUsuario

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username') 
            constrasenia = formulario.cleaned_data.get('password') 
            
            
            usuario = authenticate(username=nombre_usuario, password=constrasenia)
            
            django_login(request, usuario)
            
            return redirect('inicio:inicio')
    
    return render(request, 'usuario/login.html', {'form':formulario})


def register(request):
    
    formulario = FormularioDeRegistroDeUsuario()
    if request.method == 'POST':
        formulario = FormularioDeRegistroDeUsuario(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('usuario:login')
    
    return render(request, 'usuario/register.html', {'form':formulario})

def editar_perfil(request):
    formulario = UserChangeForm()
    return render(request, 'usuario/editar_perfil.html', {'form':formulario}) 
