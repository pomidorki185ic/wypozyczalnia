from django import forms
from .models import Notatka


class NotatkaForm(forms.ModelForm):
     class Meta:
        model = Notatka
        fields = ['opis', 'status', 'data_wykonania']

