from django.db import models
from django.forms import ModelForm

class Notatka(models.Model):
    opis = models.CharField(max_length=200)
    status = models.CharField(max_length=25, default="Do zrobienia")
    data_wykonania = models.DateField()





class NotatkaForm(ModelForm):
    class Meta:
        model = Notatka
        fields = ['opis', 'status', 'data_wykonania']