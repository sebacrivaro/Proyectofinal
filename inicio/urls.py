from django.urls import path
from inicio.views import inicio, crear_equipo, buscar_equipo

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear-equipo/', crear_equipo, name='crear_equipo'), 
    path('buscar-equipo/', buscar_equipo, name='buscar_equipo'),   
]