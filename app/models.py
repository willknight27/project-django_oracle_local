from django.db import models

# MODELOS

class Vehiculo(models.Model):

    patente = models.CharField(primary_key=True,max_length=6,verbose_name='Patente')
    marca = models.CharField(max_length=30,verbose_name='Marca')
    modelo = models.CharField(max_length=30,verbose_name='Modelo')

    def __str__(self):
        return self.patente
