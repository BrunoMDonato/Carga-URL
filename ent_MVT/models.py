from django.db import models
from django.forms import IntegerField

# Create your models here.
class Familiares(models.Model):
    dni = models.IntegerField(primary_key=True)
    edad = models.IntegerField()
    nombre = models.CharField(max_length=35)

    