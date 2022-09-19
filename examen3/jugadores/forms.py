from dataclasses import field
from socket import fromshare
from django import forms

from .models import Jugadore

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugadore
        fields = "__all__"