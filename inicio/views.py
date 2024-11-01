from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from inicio.models import Equipo
from inicio.forms import EditarEquipo, BuscarEquipo

from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio/index.html')

class CrearEquipo(CreateView):
    model = Equipo
    template_name = "inicio/crear_equipo.html"
    success_url = reverse_lazy('inicio:ver_equipo')
    fields = ['nombre_equipo', 'fundacion', 'torneos_ganados']

class ListaEquipos(ListView):
    model = Equipo
    template_name = "inicio/listado_equipos.html"
    context_object_name = 'equipos'

class VerEquipo(DetailView):
    model = Equipo
    template_name = "inicio/ver_equipo.html"
    
class EditarEquipo(UpdateView):
    model = Equipo
    template_name = "inicio/editar_equipo.html"
    success_url = reverse_lazy('inicio:listado_equipos')
    fields = ['nombre_equipo', 'fundacion', 'torneos_ganados']


class EliminarEquipo(DeleteView):
    model = Equipo
    template_name = "inicio/eliminar_equipo.html"
    success_url = reverse_lazy('inicio:listado_equipos')
    
