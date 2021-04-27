from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Asortyment
from .forms import AsortymentForm
import sets

def spis_sprzetu(request):
    obj = Asortyment.objects.all()
    query = request.GET.get('q')
    if query:
       obj = Asortyment.objects.filter(Q(nazwa__icontains=query))
    return render(request, "spis_sprzetu.html",{"obj":obj})

