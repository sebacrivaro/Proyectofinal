from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('aboutMe/', views.about, name= 'about_me'),
    
    path('equipos/', views.ListaEquipos.as_view(), name='listado_equipos'),
    path('equipos/crear/', views.CrearEquipo.as_view(), name='crear_equipo'),  
    path('equipos/<int:pk>/', views.VerEquipo.as_view(), name='ver_equipo'),       
    path('equipos/<int:pk>/editar/', views.EditarEquipo.as_view(), name='editar_equipo'),       
    path('equipos/<int:pk>/eliminar/', views.EliminarEquipo.as_view(), name='eliminar_equipo'),
    
    
    path('jugador/', views.ListaJugadores.as_view(), name= 'lista_jugadores'),       
    path('jugador/crear/', views.CrearJugador.as_view(), name= 'crear_jugador'),       
    path('jugador/<int:pk>/', views.VerJugador.as_view(), name= 'ver_jugador'),       
    path('jugador/<int:pk>/editar/', views.EditarJugador.as_view(), name= 'editar_jugador'),       
    path('jugador/<int:pk>/eliminar/', views.EliminarJugador.as_view(), name= 'eliminar_jugador'),       
]