from django.db import models
from django.forms import ModelForm
from django.core.validators import RegexValidator



class Klient(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    nr_dokumentu = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=50, null=True, blank=True)
    nr_telefonu = models.CharField(max_length=17, blank=True)
 

class KlientForm(ModelForm):
      
        class Meta:
             model = Klient
             fields = ['imie', 'nazwisko', 'nr_dokumentu','e_mail','nr_telefonu']
  