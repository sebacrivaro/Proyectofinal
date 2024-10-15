from django import forms

class CrearJugadorForm(forms.Form):
    
    edad = forms.IntegerField()
    nombre = forms.CharField(max_length=30)
    equipo_nba = forms.CharField(max_length=20)
    
class CrearEquipoForm(forms.Form):
    
    nombre_equipo = forms.CharField(max_length=20)
    fundacion = forms.IntegerField()
    torneos_ganados = forms.IntegerField()
    
class BuscarJugadorPorEquipo(forms.Form):
    equipo_nba = forms.CharField(max_length=20, required= False)