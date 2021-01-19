from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from profilKlienta.views import spis_klientow


urlpatterns = [
     path('wypozyczenie', views.wypozyczenie, name = 'wypozyczenie'),

    
   
   # path('profilKlienta/rejestracja', views.rejestracja, name = 'profilKlienta/rejestracja'),
    #path('profilKlienta/profilKlienta/rejestracja', views.AboutView, name = 'home'),
]
