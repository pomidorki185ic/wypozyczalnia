from django.db import models
from django.forms import ModelForm
from profilKlienta.models import Klient
from sprzet.models import Asortyment



class Wypozyczenie(models.Model):
     informacje_dodatkowe = models.CharField(max_length=150,default="Brak informacji dodatkowych")
     data_rozpoczecia = models.DateField()
     data_zakonczenia = models.DateField()
     godzina_rozpoczecia = models.TimeField()
     godzina_zakonczenia = models.TimeField()
     status = models.CharField(max_length=20, default="brak")
     sprzet = models.ForeignKey(Asortyment, on_delete=models.CASCADE)
     klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
     id_klient = models.CharField(max_length=20,default=1)
     id_sprzet = models.CharField(max_length=20,default=1)
     platnosc = models.CharField(max_length=6,default=0)
     rodzaj_platnosci = models.CharField(max_length=30,default='brak')
     status_platnosci = models.CharField(max_length=30,default='Do zaplaty')
     data_platnosci = models.DateField(default='1970-01-01')
  

class WypozyczenieForm(ModelForm):
    class Meta:
        model = Wypozyczenie
        fields = ['informacje_dodatkowe','data_rozpoczecia', 'data_zakonczenia', 'godzina_rozpoczecia','godzina_zakonczenia','status','sprzet','klient','id_klient','id_sprzet','platnosc','rodzaj_platnosci','status_platnosci','data_platnosci']