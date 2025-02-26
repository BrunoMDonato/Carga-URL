from django.shortcuts import render
from ent_MVT.models import *

# Create your views here.
def familia(request, dni, edad, nombre):
    dni = int(dni)
    edad = int(edad)
    familia = Familiares(dni=dni, edad=edad, nombre=nombre)
    familia.save()
    return render(request, 'base.html', {'nombre': familia})


def inicio(request):
    return render( request, 'base1.html')
