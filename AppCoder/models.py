from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=500)
