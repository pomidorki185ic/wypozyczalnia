from django import forms
from .models import Asortyment


class AsortymentForm(forms.ModelForm):
    class Meta:
        model = Asortyment
        fields = ['id','nazwa','cena_godzina','nr_seryjny','dostepnosc','informacje_awaria']

