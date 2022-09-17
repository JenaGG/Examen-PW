from django.contrib import admin

from .models import Equipo, Estadio, Jugadore
# Register your models here.

admin.site.register(Equipo)

admin.site.register(Jugadore)

admin.site.register(Estadio)