from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuario.forms import FormularioDeRegistroDeUsuario, FormularioDeEdicion
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User

from usuario.models import DatosExtra

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            
            django_login(request, usuario)
            
            DatosExtra.objects.get_or_create(user=usuario)
            
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


@login_required
def editar_perfil(request):
    datos_extra = request.user.datosextra
    
    formulario = FormularioDeEdicion(instance=request.user, initial={
        'avatar': datos_extra.avatar, 
        'edad': datos_extra.edad, 
        'equipo_fav': datos_extra.equipo_fav, 
        'deporte_fav': datos_extra.deporte_fav
        }
    )
    
    if request.method =='POST':
        formulario = FormularioDeEdicion(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            new_avatar = formulario.cleaned_data.get('avatar')
            new_edad = formulario.cleaned_data.get('edad')
            new_equipo_fav = formulario.cleaned_data.get('equipo_fav')
            new_deporte_fav = formulario.cleaned_data.get('deporte_fav')
            
            datos_extra.avatar = new_avatar if new_avatar else datos_extra.avatar
            datos_extra.edad = new_edad if new_edad else datos_extra.edad
            datos_extra.equipo_fav = new_equipo_fav if new_equipo_fav else datos_extra.equipo_fav
            datos_extra.deporte_fav = new_deporte_fav if new_deporte_fav else datos_extra.deporte_fav
            datos_extra.save()
            
            formulario.save()
            
            return redirect('inicio:inicio')
            
            
    return render(request, 'usuario/editar_perfil.html', {'form':formulario}) 

class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuario/cambiar_password.html'
    success_url = reverse_lazy('usuario:editar_perfil')
    
class VerUsuario(DetailView):
    model = User
    template_name = "usuario/ver_perfil.html"
    context_object_name = 'usuario'
    
    def get_object(self):
        return get_object_or_404(User, username = self.kwargs['username'])