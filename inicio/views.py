from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from inicio.models import Equipo
from inicio.forms import EditarEquipo, BuscarEquipo

from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio/index.html')

<<<<<<< HEAD
def team(request):
=======
@login_required
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

@login_required
def buscar_equipo(request):
    
>>>>>>> 0d34508bb02f4d232c84a2473320fef391d90e6c
    formulario = BuscarEquipo(request.GET)
    
    if formulario.is_valid():
        lista_equipos = Equipo.objects.filter(nombre_equipo__icontains=formulario.cleaned_data.get('nombre_equipo',''))
    
    return render(request, 'inicio/equipo.html',{'form':formulario, 'equipos':lista_equipos})


class CrearEquipo(CreateView):
    model = Equipo
    template_name = 'inicio/crear_equipo.html'
    fields = ['nombre_equipo', 'fundacion', 'torneos_ganados']
    success_url = reverse_lazy('inicio/equipo.html')
    
def eliminar_equipo(request, id_equipo):
        equipo = Equipo.objects.get(id=id_equipo)
        equipo.delete
        return redirect('inicio:buscar_equipo') 
    
def editar_equipo(request, id_equipo):
    equipo = Equipo.objects.get(id=id_equipo)
    formulario = EditarEquipo(initial={'nombre_equipo':equipo.nombre_equipo, 'fundacion':equipo.fundacion, 'torneos_ganados':equipo.torneos_ganados})
    if request.method == 'POST':
        formulario = EditarEquipo(request.POST)
        if formulario.is_valid():
            
            equipo.nombre_equipo = formulario.cleaned_data['nombre_equipo']
            equipo.fundacion = formulario.cleaned_data['fundacion']
            equipo.torneos_ganados = formulario.cleaned_data['torneos_ganados']
            
            equipo.save()
            
            return redirect('inicio:equipo')
        
    return render(request, 'inicio/editar_equipo.html', {'form':formulario})

class VerEquipo(DetailView):
    model = Equipo
    template_name = 'inicio/listado_equipos.html'
