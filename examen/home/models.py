from sqlite3 import Timestamp
from unittest.util import _MAX_LENGTH
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

class Jugadore(models.Model):
    Nombre=models.CharField(max_length=50)
    Edad = models.IntegerField()
    Numero = models.IntegerField()
    Equipo_perteneciente = models.CharField(max_length=50)
    Fecha_de_ingreso_al_equipo = models.DateField()
    Estatus = models.BooleanField(default=True)

    def __str__(self):
        return self.Nombre

class Estadio(models.Model):
    Nombre = models.CharField(max_length=50)
    Capacidad = models.IntegerField()
    Disponible = models.BooleanField()
    Partido_a_disputar = models.CharField(max_length=100)
    Fecha = models.DateField()

    def __str__(self):
        return self.Nombre