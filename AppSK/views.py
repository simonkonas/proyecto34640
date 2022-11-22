from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
from django.template import Template, loader

# Create your views here.

def familia(request):
    
    familiar1 = Familiar(nombre = 'Simón', apellido = 'Konaszczuk', edad = 27, cumple = '3/6/1995')
    familiar2 = Familiar(nombre = 'Jorge', apellido = 'Konaszczuk', edad = 57, cumple = '7/1/1965')
    familiar3 = Familiar(nombre = 'Elena', apellido = 'Wieczorko', edad = 57, cumple = '14/1/1965')

    
    diccionario = {'nombre1': familiar1.nombre, 'apellido1': familiar1.apellido, 'edad1': familiar1.edad, 'cumple1': familiar1.cumple,
                   'nombre2': familiar2.nombre, 'apellido2': familiar2.apellido, 'edad2': familiar2.edad, 'cumple2': familiar2.cumple,
                   'nombre3': familiar3.nombre, 'apellido3': familiar3.apellido, 'edad3': familiar3.edad, 'cumple3': familiar3.cumple
    }

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario) #documento = plantilla.render(familiar1, familiar2, familiar3)

    return HttpResponse(documento)