from errno import EDEADLK
from django.db import models

class Familiares(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha_de_nacimiento=models.DateField()
