from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('team/', views.team, name='team'),
    path('equipo/crear/', views.CrearEquipo.as_view(), name='crear_equipo'),  
    path('equipo/<int:pk>/', views.VerEquipo.as_view(), name='ver_equipo'),
    path('equipo/eliminar/', views.eliminar_equipo, name='eliminar_equipo'),  
    path('equipo/editar/', views.editar_equipo, name='editar_equipo'),  
]
