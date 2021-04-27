from django.urls import path
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
     path('spis_sprzetu', views.spis_sprzetu, name = 'spis_sprzetu'),
    
   
   # path('profilKlienta/rejestracja', views.rejestracja, name = 'profilKlienta/rejestracja'),
    #path('profilKlienta/profilKlienta/rejestracja', views.AboutView, name = 'home'),
]
