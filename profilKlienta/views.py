from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import KlientForm, SzukajKlientaForm
from .models import Klient
import sets

def rejestracja(request):
    
    if request.method == 'POST':
        form = KlientForm(request.POST)
        if form.is_valid():
            klient = form.save(commit=True)
            klient.save()
            return redirect('base')
    else:
        form = KlientForm()

    return render(request, 'rejestracja.html', {'form': form})

def base(request):
    return render(request, 'base.html', {})
def roboczy(request):
    return render(request, 'roboczy.html', {})


def spis_klientow(request):
    obj = Klient.objects.all()
    query = request.GET.get('q')
    if query:
       obj = Klient.objects.filter(Q(imie__icontains=query) | Q(nazwisko__icontains=query))
    return render(request, "spis_klientow.html",{"obj":obj})

def szukaj_klienta(request):
    template = 'spis_klientow.html'
    query = request.GET.get('q')
    obj = Klient.objects.filter(Q(imie__icontains=query) | Q(nazwisko__icontains=query))
    return render(request, template, {"obj":obj})