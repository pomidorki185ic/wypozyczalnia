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
    obj = Klient.objects.all()
    query = request.GET.get('q')
    if query:
        obj = Klient.objects.filter(Q(imie__icontains=query) | Q(nazwisko__icontains=query))
    obj1 = Asortyment.objects.all()
    query1 = request.GET.get('q1')
    if query1:
       obj1 = Asortyment.objects.filter(Q(nazwa__icontains=query1) | Q(nr_seryjny__icontains=query1))

    if request.method == 'POST':
        form = WypozyczenieForm(request.POST)
        form1 = AsortymentForm(request.POST)
        if form.is_valid():
            asortyment = form.save(commit=True)
            asortyment.save()
            Wypozyczenie = form.save(commit=True)
            Wypozyczenie.save()
            return redirect('base')
    else:
        form1 = AsortymentForm()
        form = WypozyczenieForm()
    return render(request, 'wypozyczenie.html', {"form1": form1,"form": form,"obj":obj,"obj1":obj1})


