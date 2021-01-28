from django import forms
from django.core.validators import RegexValidator
from .models import Klient

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.')

class KlientForm(forms.ModelForm):
    class Meta:
         model = Klient
         fields = ['imie', 'nazwisko', 'nr_dokumentu','e_mail','nr_telefonu','rodzaj_dok','miesiac_dok','rok_dok']

class SzukajKlientaForm(forms.ModelForm):
    class Meta:
         model = Klient
         fields = ['imie', 'nazwisko']