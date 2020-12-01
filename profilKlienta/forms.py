from django import forms

class klientForm(forms.Form):
    imie = forms.CharField(label='Twoje imie', max_length=50)
    nazwisko = forms.CharField(label='Nazwisko',max_length=50)
    nr_dokumentu = forms.CharField(label='Numer dokumentu',max_length=50)
    e_mail = forms.EmailField(label='e-mail',max_length=50, required = False)