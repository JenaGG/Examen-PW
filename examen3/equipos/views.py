from audioop import reverse
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Equipo
from .forms import EquipoForm
# Create your views here.


def index(request):
    context = {
    }
    return render(request, "home/index.html", context)

class CreateEquipo(generic.CreateView):
    template_name = "Equipos/create_equipo.html"
    model = Equipo
    form_class = EquipoForm
    success_url = reverse_lazy("equipos:list_equipo")

class ListEquipo(generic.ListView):
    template_name = "Equipos/list_equipos.html"
    queryset = Equipo.objects.filter(Clasificado=True)


class DetailEquipo(generic.DetailView):
    template_name = "equipos/detail_equipo.html"
    model = Equipo


class UpdateEquipo(generic.UpdateView):
    template_name = "equipos/update_equipo.html"
    model = Equipo
    fields = "__all__"
    success_url = reverse_lazy("equipos:list_equipo")



def delete_equipo(request, pk):
    equipo = Equipo.objects.get(pk=pk, Clasificado=True)
    equipo.Clasificado = False
    equipo.save()
    messages.warning(request, "Fuiste descalificado de la temporada :(")
    return redirect("equipos:list_equipo")
