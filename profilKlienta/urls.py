"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
     path('', views.base, name = 'base'),
     path('rejestracja', views.rejestracja, name = 'rejestracja'),
     path('spis_klientow', views.spis_klientow, name = 'spis_klientow'),
     path('spis_klientow/<int:pk>/', views.dane_klienta, name = 'dane_klienta'),
     path('platnosci', views.platnosci, name = 'platnosci'),
     path('historia', views.historia, name = 'historia'),
     path('dane_wypozyczenia/<int:pk>/', views.dane_wypozyczenia, name = 'dane_wypozyczenia'),
     path('dane_sprzetu/<int:pk>/', views.dane_sprzetu, name = 'dane_sprzetu'),
     path('dostawy', views.dostawy, name = 'dostawy'),
     path('awarie', views.awarie, name = 'awarie'),
     path('dane_awaria/<int:pk>/', views.dane_awaria, name = 'dane_awaria'),
     
   
   # path('profilKlienta/rejestracja', views.rejestracja, name = 'profilKlienta/rejestracja'),
    #path('profilKlienta/profilKlienta/rejestracja', views.AboutView, name = 'home'),
]
