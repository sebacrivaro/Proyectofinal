from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('equipos/', views.ListaEquipos.as_view(), name='listado_equipos'),
    path('equipos/crear/', views.CrearEquipo.as_view(), name='crear_equipo'),  
    path('equipos/<int:pk>/', views.VerEquipo.as_view(), name='ver_equipo'),       
    path('equipos/<int:pk>/editar/', views.EditarEquipo.as_view(), name='editar_equipo'),       
    path('equipos/<int:pk>/eliminar/', views.EliminarEquipo.as_view(), name='eliminar_equipo'),       
]

