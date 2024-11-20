from django.urls import path 
from usuario import views
from django.contrib.auth.views import LogoutView

app_name ='usuario'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/<str:username>/', views.VerUsuario.as_view(), name='ver_perfil'),
    path('perfil/editar/password/', views.CambiarPassword.as_view(), name='cambiar_password'),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
]
