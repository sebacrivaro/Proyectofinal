from django.urls import path 
from usuario import views
from django.contrib.auth.views import LogoutView

app_name ='usuario'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
<<<<<<< HEAD
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
=======
>>>>>>> 0d34508bb02f4d232c84a2473320fef391d90e6c
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
]
