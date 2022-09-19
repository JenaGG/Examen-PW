from django.db import models

# Create your models here.

class Estadio(models.Model):
    Nombre = models.CharField(max_length=50)
    Capacidad = models.IntegerField()
    Disponible = models.BooleanField()
    Partido_a_disputar = models.CharField(max_length=100)
    Fecha = models.DateField()

    def __str__(self):
        return self.Nombre