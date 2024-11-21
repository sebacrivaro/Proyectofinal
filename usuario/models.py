from django.db import models
from django.contrib.auth.models import User


class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', blank=True, null= True)
    edad = models.IntegerField(null=True, blank=True)
    equipo_fav = models.CharField(max_length=20)
    deporte_fav = models.CharField(max_length=20)

