from django.http import HttpResponse
from django.shortcuts import render, redirect

from inicio.models import Equipo
from inicio.forms import CrearEquipoForm, BuscarEquipo

def inicio(request):
    return render(request, 'inicio/index.html')


def crear_equipo(request):
    formulario = CrearEquipoForm()
    
    if request.method == 'POST':
        formulario = CrearEquipoForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            equipo = Equipo(nombre_equipo = data.get('nombre_equipo'), fundacion = data.get('fundacion'), torneos_ganados = data.get('torneos_ganados'))
            equipo.save()
            return redirect('inicio:buscar_equipo')
    
    
    return render(request, 'inicio/crear_equipo.html', {'form':formulario})

def buscar_equipo(request):
    
    formulario = BuscarEquipo(request.GET)
    if formulario.is_valid():
        nombre_equipo= formulario.cleaned_data.get('nombre_equipo') 
        equipos = Equipo.objects.filter(nombre_equipo__icontains=nombre_equipo)
    
    return render(request, 'inicio/buscar_equipo.html', {'equipos':equipos, 'form':formulario})