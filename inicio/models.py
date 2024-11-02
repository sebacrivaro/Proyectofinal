from django.db import models

# Create your models here.

        
class Equipo(models.Model):
    
    nombre_equipo = models.CharField(max_length=20)
    fundacion = models.IntegerField()
    torneos_ganados = models.IntegerField()
    
    def __str__(self):
        return (f'id:{self.id}, Nombre del equipo:{self.nombre_equipo}, Fundacion:{self.fundacion}, Cantidad de torneos:{self.torneos_ganados}')