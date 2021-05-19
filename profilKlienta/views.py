from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .forms import KlientForm, SzukajKlientaForm
from sprzet.forms import AsortymentForm
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
    wczoraj = date.today() - timedelta(days=1)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    klient = Klient.objects.all()
    
    rezerwacja = Wypozyczenie.objects.all()
    powrot = Wypozyczenie.objects.all()
    spoznienia = Wypozyczenie.objects.all()
    d1 = today.strftime("%Y-%m-%d")
    if d1 and current_time:
        powrot = Wypozyczenie.objects.order_by('data_zakonczenia').filter(Q(data_zakonczenia__icontains=d1) & Q(godzina_zakonczenia__gte=current_time) & Q(status__icontains="Pickup") | Q(data_zakonczenia__icontains=jutro) & Q(status__icontains="Pickup"))

    if d1 and current_time:
        rezerwacja = Wypozyczenie.objects.order_by('data_rozpoczecia').filter(Q(data_rozpoczecia__icontains=d1) & Q(godzina_rozpoczecia__gte=current_time) & Q(status__icontains="Rezerwacja") | Q(data_rozpoczecia__icontains=jutro) & Q(status__icontains="Rezerwacja") | Q(data_rozpoczecia__icontains=d1) & Q(godzina_rozpoczecia__lte=current_time) & Q(status__icontains="Rezerwacja"))

    if d1 and current_time:
        spoznienia = Wypozyczenie.objects.order_by('data_zakonczenia').filter(Q(data_zakonczenia__lte=d1) & Q(godzina_zakonczenia__lte=current_time) & Q(status__icontains="Pickup") | Q(data_zakonczenia__lte=wczoraj) & Q(status__icontains="Pickup") )
   
    return render(request, 'Dashboard.html', {"powrot":powrot,"rezerwacja":rezerwacja,"spoznienia":spoznienia,"klient":klient})




def dane_wypozyczenia(request, pk):
    
    klient = Klient.objects.all()
    
    wypozyczenie = get_object_or_404(Wypozyczenie, pk=pk)
    if request.method == 'POST':
        form = WypozyczenieForm(request.POST, instance=wypozyczenie)
        sprzetId = request.POST.get('id_sprzet')
        if form.is_valid():
            rower = Asortyment.objects.get(id=sprzetId)
            rower.dostepnosc = 'Dostepny'
            rower.save()
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
    obj = Klient.objects.order_by('pk').reverse().all()
    query = request.GET.get('q')
    if query:
       obj = Klient.objects.order_by('pk').reverse().filter(Q(pk__icontains=query) | Q(imie__icontains=query) | Q(nazwisko__icontains=query))
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

    dostawyDzisiaj = Wypozyczenie.objects.order_by('pk').reverse().all()
    dostawyJutro =  Wypozyczenie.objects.order_by('pk').reverse().all()

    rezerwacja = Wypozyczenie.objects.order_by('pk').reverse().all()
    powrot = Wypozyczenie.objects.order_by('pk').reverse().all()
    spoznienia = Wypozyczenie.objects.order_by('pk').reverse().all()
    d1 = today.strftime("%Y-%m-%d")

    if d1 and current_time:
        dostawyDzisiaj = Wypozyczenie.objects.order_by('pk').reverse().filter(Q(data_rozpoczecia__icontains=d1) & Q(godzina_rozpoczecia__gte=current_time) & Q(status__icontains="Dostawa") )

    if d1 and current_time:
        dostawyJutro = Wypozyczenie.objects.order_by('pk').reverse().filter( Q(data_rozpoczecia__icontains=jutro) & Q(status__icontains="Dostawa"))

    if query:
        dostawyDzisiaj = Wypozyczenie.objects.order_by('pk').reverse().filter(Q(data_rozpoczecia__icontains=query) & Q(status__icontains="Dostawa") )

    if query1:
        dostawyJutro = Wypozyczenie.objects.order_by('pk').reverse().filter( Q(data_rozpoczecia__icontains=query1) & Q(status__icontains="Dostawa"))
   
    return render(request, 'dostawy.html', {"dostawyDzisiaj":dostawyDzisiaj,"dostawyJutro":dostawyJutro})

def dane_sprzetu(request, pk):
    sprzet = get_object_or_404(Asortyment, pk=pk)
    if request.method == 'POST':
        form = AsortymentForm(request.POST, instance=sprzet)
        if form.is_valid():
            sprzet = form.save(commit=True)
            sprzet.save()
            return redirect('spis_sprzetu')
    else:
        form = AsortymentForm(instance=sprzet)
    return render(request, "dane_sprzetu.html",{'form': form,"sprzet":sprzet})

def awarie(request):
     obj = Asortyment.objects.order_by('pk').filter(Q(dostepnosc__contains="Awaria"))
     return render(request, "awarie.html",{"obj":obj})

def dane_awaria(request, pk):
    sprzet = get_object_or_404(Asortyment, pk=pk)
    if request.method == 'POST':
        form = AsortymentForm(request.POST, instance=sprzet)
        if form.is_valid():
            sprzet = form.save(commit=True)
            sprzet.save()
            return redirect('awarie')
    else:
        form = AsortymentForm(instance=sprzet)
    return render(request, "dane_awaria.html",{'form': form,"sprzet":sprzet})