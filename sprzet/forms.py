from django import forms
from .models import Asortyment


class AsortymentForm(forms.ModelForm):
    class Meta:
        model = Asortyment
        fields = ['id','cena_godzina','dostepnosc']

