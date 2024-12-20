from django import forms

class EditarEquipo(forms.Form):
    
    nombre_equipo = forms.CharField(max_length=20)
    fundacion = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    torneos_ganados = forms.IntegerField()
    escudo = forms.ImageField(required=False)
    
    
class BuscarEquipo(forms.Form):
    nombre_equipo = forms.CharField(max_length=20, required= False)
    
class EditarJugador(forms.Form):
    
    nombre = forms.CharField(max_length=20)
    numero_jugador = forms.IntegerField()
    equipo_que_milita = forms.CharField(max_length=20)