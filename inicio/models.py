from django.db import models

# Create your models here.

        
class Equipo(models.Model):
    
    nombre_equipo = models.CharField(max_length=20)
    fundacion = models.IntegerField()
    torneos_ganados = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre_equipo} {self.fundacion} {self.torneos_ganados}'