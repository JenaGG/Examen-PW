from audioop import reverse
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Estadio
from .forms import EstadioForm
# Create your views here.


class CreateEstadio(generic.CreateView):
    template_name = "Estadios/create_estadio.html"
    model = Estadio
    form_class = EstadioForm
    success_url = reverse_lazy("estadios:list_estadio")


class ListEstadio(generic.ListView):
    template_name = "Estadios/list_estadio.html"
    queryset = Estadio.objects.filter(Disponible=True)


class DetailEstadio(generic.DetailView):
    template_name = "estadios/detail_estadio.html"
    model = Estadio


class UpdateEstadio(generic.UpdateView):
    template_name = "estadios/update_estadio.html"
    model = Estadio
    fields = "__all__"
    success_url = reverse_lazy("estadios:list_estadio")



def delete_estadio(request, pk):
    estadio = Estadio.objects.get(pk=pk, Disponible=True)
    estadio.Disponible = False
    estadio.save()
    messages.warning(request, "Fuiste descalificado de la temporada :(")
    return redirect("estadios:list_estadio")
