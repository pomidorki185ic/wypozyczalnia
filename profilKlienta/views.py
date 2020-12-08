from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import KlientForm

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