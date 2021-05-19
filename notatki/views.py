from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notatka
from .forms import NotatkaForm
from datetime import date, datetime, timedelta

def notatki(request):

    if request.method == 'POST':
        form = NotatkaForm(request.POST)
        if form.is_valid():
            notatka = form.save(commit=True)
            notatka.save()
            return redirect('notatki')
    else:
        form = NotatkaForm()

    notatki = Notatka.objects.order_by('pk').all()
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    if d1:
        notatki = Notatka.objects.order_by('pk').filter(Q(data_wykonania__icontains=d1) & ~Q(status="Zakończone"))

    return render(request, 'notatki.html', {'form': form, "notatki":notatki,})

def dane_notatki(request, pk):

    notatka = get_object_or_404(Notatka, pk=pk)
    if request.method == 'POST':
        form2 = NotatkaForm(request.POST, instance=notatka)
        if form2.is_valid():
            notatka = form2.save(commit=True)
            notatka.save()
            return redirect('notatki')
    else:
        form2 = NotatkaForm(instance=notatka)

    return render(request, 'dane_notatki.html', {'form2': form2,})