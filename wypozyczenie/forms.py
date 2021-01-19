from django import forms
from .models import Wypozyczenie


class WypozyczenieForm(forms.ModelForm):
    class Meta:
        model = Wypozyczenie
        fields = ['data_rozpoczecia', 'data_zakonczenia', 'godzina_rozpoczecia','godzina_zakonczenia','status','sprzet','klient']

