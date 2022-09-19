from dataclasses import field
from socket import fromshare
from django import forms

from .models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = "__all__"