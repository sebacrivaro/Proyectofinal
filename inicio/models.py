from django.db import models

# Create your models here.

class Jugador(models.Model):
    
    edad = models.IntegerField()
    nombre = models.CharField(max_length=30)
    equipo_nba = models.CharField(max_length=20)
    
class Equipo(models.Model):
    
    nombre_equipo = models.CharField(max_length=20)
    fundacion = models.IntegerField()
    torneos_ganados = models.IntegerField()