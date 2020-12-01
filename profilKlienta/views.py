from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import klientForm
from .models import Klient

def rejestracja(request):
    if request.method == 'POST':
     
        form = klientForm(request.POST)
       
        if form.is_valid():
            imie = form.cleaned_data['imie']
            nazwisko = form.cleaned_data['nazwisko']
            nr_dokumentu = form.cleaned_data['nr_dokumentu']
            e_mail = form.cleaned_data['e_mail']
            k = Klient(imie=imie,nazwisko=nazwisko,nr_dokumentu=nr_dokumentu,e_mail=e_mail)
            k.save()
            return redirect('home:home')
  
   
    return render(request, '../templates/profilKlienta/rejestracja.html', {'form': form})