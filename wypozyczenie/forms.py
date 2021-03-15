from django import forms
from .models import Wypozyczenie


class WypozyczenieForm(forms.ModelForm):
    class Meta:
        model = Wypozyczenie
        fields = ['informacje_dodatkowe','data_rozpoczecia', 'data_zakonczenia', 'godzina_rozpoczecia','godzina_zakonczenia','status','sprzet','klient','id_klient','id_sprzet','platnosc','rodzaj_platnosci','status_platnosci','data_platnosci']

