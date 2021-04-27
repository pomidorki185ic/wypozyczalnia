from django.db import models
from django.forms import ModelForm

class Asortyment(models.Model):
    nazwa = models.CharField(max_length=50)
    cena_godzina = models.CharField(max_length=5, default=15)
    nr_seryjny = models.CharField(max_length=50)
    dostepnosc = models.CharField(max_length=20, default='Dostepny')
    informacje_awaria = models.CharField(max_length=200,default="Brak informacji")
 
    def dodajSprzet(self):
        self.save()

    def __str__(self):
        return self.nazwa


class AsortymentForm(ModelForm):
    class Meta:
        model = Asortyment
        fields = ['id','nazwa','cena_godzina','nr_seryjny','dostepnosc','informacje_awaria']

