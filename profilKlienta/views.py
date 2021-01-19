from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('dane_klienta', pk=klient.pk)
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
       obj = Klient.objects.filter(Q(pk__icontains=query) | Q(imie__icontains=query) | Q(nazwisko__icontains=query))
    return render(request, "spis_klientow.html",{"obj":obj})

def dane_klienta(request, pk):
    klient = get_object_or_404(Klient, pk=pk)
    if request.method == 'POST':
        form = KlientForm(request.POST, instance=klient)
        if form.is_valid():
            klient = form.save(commit=True)
            klient.save()
            return redirect('spis_klientow')
    else:
        form = KlientForm(instance=klient)
    return render(request, "dane_klienta.html",{'form': form,"klient":klient})

