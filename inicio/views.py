from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from inicio.models import Equipo
from inicio.forms import EditarEquipo, BuscarEquipo

from inicio.models import Jugador


def inicio(request):
    return render(request, 'inicio/index.html')

def about(request):
    return render(request, 'inicio/about_me.html')

class CrearEquipo(LoginRequiredMixin, CreateView):
    model = Equipo
    template_name = "inicio/crear_equipo.html"
    success_url = reverse_lazy('inicio:listado_equipos')
    fields = ['nombre_equipo', 'fundacion', 'torneos_ganados','escudo']

class ListaEquipos(ListView):
    model = Equipo
    template_name = "inicio/listado_equipos.html"
    context_object_name = 'equipos'

class VerEquipo(DetailView):
    model = Equipo
    template_name = "inicio/ver_equipo.html"
    
class EditarEquipo(LoginRequiredMixin ,UpdateView):
    model = Equipo
    template_name = "inicio/editar_equipo.html"
    success_url = reverse_lazy('inicio:listado_equipos')
    fields = ['nombre_equipo', 'fundacion', 'torneos_ganados', 'escudo']


class EliminarEquipo(LoginRequiredMixin, DeleteView):
    model = Equipo
    template_name = "inicio/eliminar_equipo.html"
    success_url = reverse_lazy('inicio:listado_equipos')
 
class CrearJugador(LoginRequiredMixin, CreateView):
    model = Jugador
    template_name = "inicio/crear_jugador.html"
    success_url = reverse_lazy('inicio:lista_jugadores')
    fields = ['nombre', 'numero_jugador', 'equipo_que_milita']

class ListaJugadores(ListView):
    model = Jugador
    template_name = "inicio/lista_jugadores.html"
    context_object_name = 'jugadores'
    
class VerJugador(DetailView):
    model = Jugador
    template_name = "inicio/ver_jugador.html"

class EditarJugador(LoginRequiredMixin ,UpdateView):
    model = Jugador
    template_name = "inicio/editar_jugador.html"
    success_url = reverse_lazy('inicio:lista_jugadores')
    fields = ['nombre', 'numero_jugador', 'equipo_que_milita']


class EliminarJugador(LoginRequiredMixin, DeleteView):
    model = Jugador
    template_name = "inicio/eliminar_jugador.html"
    success_url = reverse_lazy('inicio:lista_jugadores')