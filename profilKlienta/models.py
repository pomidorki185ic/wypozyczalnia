from django.db import models
from django.forms import ModelForm
class Klient(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    nr_dokumentu = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=50, null=True, blank=True)
  
    class Admin:
        pass
    def __str__(self):
        return self.name

class Klientform(ModelForm):
       

        class Meta:
             model = Klient
             fields = ['imie', 'nazwisko', 'nr_dokumentu','e_mail']
  