from django.db import models

# Create your models here.

class Equipo(models.Model):
    Nombre = models.CharField(max_length=32)
    Entrenador = models.CharField(max_length=32)
    Total_de_jugadores = models.IntegerField()
    Total_de_Partidos = models.IntegerField()
    Total_de_puntos = models.IntegerField()
    Clasificado = models.BooleanField(default=False)

    def __str__(self):
        return self.Nombre