from django.http import HttpResponse
from django.shortcuts import render, redirect

from inicio.models import Jugador, Equipo
from inicio.forms import CrearEquipoForm, CrearJugadorForm, BuscarJugadorPorEquipo

def inicio(request):
    return render(request, 'inicio/index.html')



def crear_jugador(request):
    
    # print('Request', request)
    # print('GET', request.GET)
    # print('POST', request.POST)
    
    formulario = CrearJugadorForm()
    
    if request.method == 'POST':
        formulario = CrearJugadorForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            jugador = Jugador(edad = data.get('edad'), nombre = data.get('nombre'), equipo_nba = data.get('equipo'))
            jugador.save()
            return redirect('inicio:buscar_equipo')
    
    
    return render(request, 'inicio/crear_jugador.html', {'form':formulario})


def crear_equipo(request):
    formulario = CrearEquipoForm()
    
    if request.method == 'POST':
        formulario = CrearEquipoForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            equipo = Equipo(nombre_equipo = data.get('nombre'), fundacion = data.get('fundacion'), torneos_ganados = data.get('campeonatos'))
            equipo.save()
            return redirect('inicio:buscar_equipo')
    
    
    return render(request, 'inicio/crear_jugador.html', {'form':formulario})

def buscar_equipo(request):
    
    formulario = BuscarJugadorPorEquipo(request.GET)
    
    if formulario.is_valid():
        equipo_nba= formulario.cleaned_data.get('equipo') 
        if equipo_nba:
            jugadores = Jugador.objects.filter(equipo_nba__icontains=equipo_nba)
        else:
            jugadores = Jugador.objects.all()
    else:
        jugadores = Jugador.objects.all()
    
    return render(request, 'inicio/buscar_equipo.html', {'jugadores':jugadores, 'form':formulario})