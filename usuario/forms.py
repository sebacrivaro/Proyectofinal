from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class FormularioDeRegistroDeUsuario(UserCreationForm):
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contrasenia', widget=forms.PasswordInput)
    edad = forms.IntegerField()
    equipo_fav = forms.CharField(max_length=20)
    deporte_fav = forms.CharField(max_length=20)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'edad', 'equipo_fav', 'deporte_fav']
        help_texts = {key: '' for key in fields}
        
class FormularioDeEdicion(UserChangeForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password = None
    avatar = forms.ImageField(required=False)
    edad = forms.IntegerField()
    equipo_fav = forms.CharField(max_length=20)
    deporte_fav = forms.CharField(max_length=20)
    
    class Meta():
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar', 'edad', 'equipo_fav', 'deporte_fav']