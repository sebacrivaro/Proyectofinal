from django import forms

class EditarEquipo(forms.Form):
    
    nombre_equipo = forms.CharField(max_length=20)
    fundacion = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    torneos_ganados = forms.IntegerField()
    
class BuscarEquipo(forms.Form):
    nombre_equipo = forms.CharField(max_length=20, required= False)