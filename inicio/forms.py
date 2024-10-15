from django import forms

class CrearEquipoForm(forms.Form):
    
    nombre_equipo = forms.CharField(max_length=20)
    fundacion = forms.IntegerField()
    torneos_ganados = forms.IntegerField()
    
class BuscarEquipo(forms.Form):
    nombre_equipo = forms.CharField(max_length=20, required= False)