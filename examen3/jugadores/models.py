from django.db import models

# Create your models here.

class Jugadore(models.Model):
    Nombre=models.CharField(max_length=50)
    Edad = models.IntegerField()
    Numero = models.IntegerField()
    Equipo_perteneciente = models.CharField(max_length=50)
    Fecha_de_ingreso_al_equipo = models.DateField()
    Estatus = models.BooleanField(default=True)

    def __str__(self):
        return self.Nombre