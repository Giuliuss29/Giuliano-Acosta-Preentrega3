from django.db import models

class Peliculas(models.Model):
    titulo = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    
class Series(models.Model):
    titulo = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    temporadas = models.DecimalField(decimal_places=1, max_digits=3)
    
class Famosos(models.Model):
    nombre = models.CharField(max_length=255)
    profesion = models.CharField(max_length=255)       