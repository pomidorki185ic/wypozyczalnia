from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .forms import KlientForm, SzukajKlientaForm
from .models import Klient
from sprzet.models import Asortyment
from wypozyczenie.models import Wypozyczenie
from wypozyczenie.forms import WypozyczenieForm 
import sets
from datetime import date, datetime, timedelta


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
    today = date.today()
    jutro = date.today() + timedelta(days=1)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    klient = Klient.objects.all()
    
    rezerwacja = Wypozyczenie.objects.all()
    powrot = Wypozyczenie.objects.all()
    spoznienia = Wypozyczenie.objects.all()
    d1 = today.strftime("%Y-%m-%d")
    if d1 and current_time:
        powrot = Wypozyczenie.objects.filter(Q(data_zakonczenia__icontains=d1) & Q(godzina_zakonczenia__gte=current_time) & Q(status__icontains="Pickup") | Q(data_zakonczenia__icontains=jutro) & Q(status__icontains="Pickup") & Q(data_zakonczenia__icontains=d1) & Q(godzina_zakonczenia__gte=current_time) & Q(status__icontains="Dostawa") | Q(data_zakonczenia__icontains=jutro) & Q(status__icontains="Dostawa"))

    if d1 and current_time:
        rezerwacja = Wypozyczenie.objects.filter(Q(data_rozpoczecia__icontains=d1) & Q(godzina_rozpoczecia__gte=current_time) & Q(status__icontains="Rezerwacja") | Q(data_rozpoczecia__icontains=jutro) & Q(status__icontains="Rezerwacja") | Q(data_rozpoczecia__icontains=d1) & Q(godzina_rozpoczecia__lte=current_time) & Q(status__icontains="Rezerwacja"))

    if d1 and current_time:
        spoznienia = Wypozyczenie.objects.filter(Q(data_zakonczenia__lte=d1) & Q(godzina_zakonczenia__lte=current_time) & Q(status__icontains="Pickup"))
   
    return render(request, 'Dashboard.html', {"powrot":powrot,"rezerwacja":rezerwacja,"spoznienia":spoznienia,"klient":klient})




def dane_wypozyczenia(request, pk):
    
    klient = Klient.objects.all()
    
    wypozyczenie = get_object_or_404(Wypozyczenie, pk=pk)
    if request.method == 'POST':
        form = WypozyczenieForm(request.POST, instance=wypozyczenie)
        if form.is_valid():
            wypozyczenie = form.save(commit=True)
            wypozyczenie.save()
            return redirect('base')
    else:
        form = WypozyczenieForm(instance=wypozyczenie)
    query3 = request.GET.get('q3')
    if query3:
       klient = Klient.objects.filter(Q(pk__icontains=query3))
    
    return render(request, 'dane_wypozyczenia.html', {'form':form,"wypozyczenie":wypozyczenie,'klient':klient})



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

def platnosci(request):
    obj_platnosc = Wypozyczenie.objects.all()
    do_zaplaty = Wypozyczenie.objects.order_by('pk').reverse().filter(Q(status_platnosci="Do zaplaty"))
    zaplacone = Wypozyczenie.objects.order_by('pk').reverse().filter(Q(status_platnosci="Zapłacony") | Q(status_platnosci="Nadpłata"))
    query = request.GET.get('q')
    if query:
        do_zaplaty =  Wypozyczenie.objects.order_by('pk').reverse().filter(Q(data_rozpoczecia__icontains=query) & Q(status_platnosci="Do zaplaty"))

    query1 = request.GET.get('q1')
    if query1:
        zaplacone =  Wypozyczenie.objects.order_by('pk').reverse().filter(Q(data_platnosci__icontains=query1) & Q(status_platnosci="Zapłacony") | Q(data_platnosci__icontains=query1) & Q(status_platnosci="Nadpłata"))
    return render(request, "platnosci.html",{'do_zaplaty':do_zaplaty,'zaplacone':zaplacone})

def historia(request):
    historia = Wypozyczenie.objects.order_by('pk').all().reverse()
    query = request.GET.get('q')
    if query:
        historia = Wypozyczenie.objects.order_by('pk').reverse().filter(Q(data_rozpoczecia__icontains=query))
    return render(request, "historia.html",{'historia':historia})


def dostawy(request):
    today = date.today()
    jutro = date.today() + timedelta(days=1)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    query = request.GET.get('q')
    query1 = request.GET.get('q1')

    dostawyDzisiaj = Wypozyczenie.objects.all()
    dostawyJutro =  Wypozyczenie.objects.all()

    rezerwacja = Wypozyczenie.objects.all()
    powrot = Wypozyczenie.objects.all()
    spoznienia = Wypozyczenie.objects.all()
    d1 = today.strftime("%Y-%m-%d")

    if d1 and current_time:
        dostawyDzisiaj = Wypozyczenie.objects.filter(Q(data_rozpoczecia__icontains=d1) & Q(godzina_rozpoczecia__gte=current_time) & Q(status__icontains="Dostawa") )

    if d1 and current_time:
        dostawyJutro = Wypozyczenie.objects.filter( Q(data_rozpoczecia__icontains=jutro) & Q(status__icontains="Dostawa"))

    if query:
        dostawyDzisiaj = Wypozyczenie.objects.filter(Q(data_rozpoczecia__icontains=query) & Q(status__icontains="Dostawa") )

    if query1:
        dostawyJutro = Wypozyczenie.objects.filter( Q(data_rozpoczecia__icontains=query1) & Q(status__icontains="Dostawa"))
   
    return render(request, 'dostawy.html', {"dostawyDzisiaj":dostawyDzisiaj,"dostawyJutro":dostawyJutro})