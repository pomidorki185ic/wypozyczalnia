from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Asortyment
import sets

def spis_sprzetu(request):
    obj = Asortyment.objects.all()
    query = request.GET.get('q')
    if query:
       obj = Asortyment.objects.filter(Q(nazwa__icontains=query) | Q(nr_seryjny__icontains=query) | Q(rodzaj__icontains=query))
    return render(request, "spis_sprzetu.html",{"obj":obj})

