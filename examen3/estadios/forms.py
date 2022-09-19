from dataclasses import field
from socket import fromshare
from django import forms

from .models import Estadio

class EstadioForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = "__all__"