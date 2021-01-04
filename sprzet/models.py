from django.db import models


class Asortyment(models.Model):
    rodzaj = models.CharField(max_length=50)
    nazwa = models.CharField(max_length=50)
    nr_seryjny = models.CharField(max_length=50)
 
    def dodajSprzet(self):
        self.save()

    def __str__(self):
        return self.nazwa

