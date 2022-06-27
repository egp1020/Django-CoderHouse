from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random

def saludo(request):
    return HttpResponse("Hello coder!")

def saludo_particular(request, nombre):
    return HttpResponse(f"Hello, {nombre.capitalize()}")

def fecha_nacimiento(request, edad):
    fecha_actual = datetime.now()
    return HttpResponse(f"Hello el año de nacimiento es {fecha_actual.year - int(edad)}")

def template_saludo_general(request):
    return render(request, "saludo/index.html")

def calcular_imc(request):
    context = {
        "imc": 0
    }

    if request.GET:
        altura = float(request.GET['altura'])
        peso = float(request.GET['peso'])

        context['imc'] = peso /( altura * altura)

    return render(request, "imc/index.html", context)

def elegir_nombre_aleatorio(request):
    context = {
        "nombres": [],
        "elegido": ""
    }

    if request.GET:
        context['nombres'] = request.GET['nombres'].split()
        context['elegido'] = random.choice(context['nombres'])

    return render(request, "nombre_aleatorio/index.html", context)