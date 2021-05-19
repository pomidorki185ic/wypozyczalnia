from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from profilKlienta.models import Klient
from sprzet.models import  Asortyment
from .forms import WypozyczenieForm
from .models import Wypozyczenie
from sprzet.forms import AsortymentForm
import sets

def wypozyczenie(request):
    obj = Klient.objects.order_by('pk').filter(~Q(imie__icontains='Usuniete'))
    query = request.GET.get('q')
    if query:
        obj = Klient.objects.order_by('pk').filter(Q(imie__icontains=query) & ~Q(imie__icontains='Usuniete') | Q(nazwisko__icontains=query) & ~Q(imie__icontains='Usuniete'))
    obj1 = Asortyment.objects.order_by('pk').filter(Q(dostepnosc__contains="Dostepny"))
    query1 = request.GET.get('q1')

    if query1:
       obj1 = Asortyment.objects.order_by('pk').filter(Q(nazwa__icontains=query1) | Q(nr_seryjny__icontains=query1)) 

    if request.method == 'POST':
        sprzetId = request.POST.get('sprzet')
        form = WypozyczenieForm(request.POST)
        form1 = AsortymentForm(request.POST)
        if form.is_valid():
            rower = Asortyment.objects.get(id=sprzetId)
            rower.dostepnosc = 'Wypozyczone'
            rower.save()

            Wypozyczenie = form.save(commit=True)
            Wypozyczenie.save()
            return redirect('base')
    else:
        form1 = AsortymentForm()
        form = WypozyczenieForm()
    return render(request, 'wypozyczenie.html', {"form1": form1,"form": form,"obj":obj,"obj1":obj1})