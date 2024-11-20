from django.db import models

# Create your models here.

        
class Equipo(models.Model):
    
    nombre_equipo = models.CharField(max_length=20)
    fundacion = models.DateField()
    torneos_ganados = models.IntegerField()
    escudo = models.ImageField(upload_to='escudos', blank=True, null= True)
    
    def __str__(self):
        return (f'id:{self.id}, Nombre del equipo:{self.nombre_equipo}, Fundacion:{self.fundacion}, Cantidad de torneos:{self.torneos_ganados}')
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=20)
    numero_jugador = models.IntegerField()
    equipo_que_milita = models.CharField(max_length=20)
    
    def __str__(self):
        return (f'id:{self.id}, Nombre del jugador:{self.nombre}, Numero de camiseta:{self.numero_jugador}, Equipo donde juega:{self.equipo_que_milita}')