from audioop import reverse
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Jugadore
from .forms import JugadorForm
# Create your views here.


class Createjugador(generic.CreateView):
    template_name = "jugadores/create_jugador.html"
    model = Jugadore
    form_class = JugadorForm
    success_url = reverse_lazy("jugadores:list_jugador")


class Listjugador(generic.ListView):
    template_name = "jugadores/list_jugador.html"
    queryset = Jugadore.objects.filter(Estatus=True)


class Detailjugador(generic.DetailView):
    template_name = "jugadores/detail_jugador.html"
    model = Jugadore


class Updatejugador(generic.UpdateView):
    template_name = "jugadores/update_jugador.html"
    model = Jugadore
    fields = "__all__"
    success_url = reverse_lazy("jugadores:list_jugador")



def delete_jugador(request, pk):
    jugador = Jugadore.objects.get(pk=pk, Estatus=True)
    jugador.Estatus = False
    jugador.save()
    messages.warning(request, "Fuiste descalificado de la temporada :(")
    return redirect("jugadores:list_jugador")
