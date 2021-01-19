from django.db import models
from django.forms import ModelForm
from profilKlienta.models import Klient
from sprzet.models import Asortyment



class Wypozyczenie(models.Model):
     data_rozpoczecia = models.DateField()
     data_zakonczenia = models.DateField()
     godzina_rozpoczecia = models.TimeField()
     godzina_zakonczenia = models.TimeField()
     status = models.CharField(max_length=20, default="brak")
     sprzet = models.ForeignKey(Asortyment, on_delete=models.CASCADE)
     klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
  

class WypozyczenieForm(ModelForm):
    class Meta:
        model = Wypozyczenie
        fields = ['data_rozpoczecia', 'data_zakonczenia', 'godzina_rozpoczecia','godzina_zakonczenia','status','sprzet','klient']