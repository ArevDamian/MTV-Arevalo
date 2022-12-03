from django.shortcuts import render
from django.http import HttpResponse
from MyBus.models import Colectivo, Recorrido, Tarifa
from django.core import serializers
from MyBus.forms import *

# Create your views here.
def Principal(request):
    return render(request, 'MyBus/principal.html')

def busqueda(request):
    return render(request, 'MyBus/busqueda.html')

def buscar(request):
    codigo = request.GET['linea_colectivo']
    lineas_todas = Colectivo.objects.filter(linea_colectivo=codigo)
    #return HttpResponse (f'Esta es la linea {codigo} que tiene estos destinos:')
    return render(request, 'MyBus/resultado.html', {"colectivo":codigo, "colectivos_todos":lineas_todas})

def colectivo(request):
    if request.method == "POST":
        miFormulario = ColectivoFormulario(request.POST)  
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            colectivo = Colectivo(linea_colectivo=informacion["linea_colectivo"], numero_colectivo=informacion["numero_colectivo"])
            colectivo.save()
            return render (request, "MyBus/Principal.html")
    else:
        miFormulario=ColectivoFormulario()
    return render (request, "MyBus/colectivo.html", {"miFormulario": miFormulario})


def recorrido(request):
    if request.method == "POST":
        miFormulario = RecorridoFormulario(request.POST)  
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            recorrido = Recorrido(linea_colectivo=informacion["linea_colectivo"], inicio=informacion["inicio"], destino=informacion["destino"], minutos_viaje=informacion["minutos_viaje"])
            recorrido.save()
            return render (request, "MyBus/Principal.html")
    else:
        miFormulario=RecorridoFormulario()
    return render (request, "MyBus/recorrido.html", {"miFormulario": miFormulario})

def tarifa(request):
    if request.method == "POST":
        miFormulario = TarifaFormulario(request.POST)  
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            tarifa = Tarifa(linea_colectivo=informacion["linea_colectivo"], valor_pasaje=informacion["valor_pasaje"])
            tarifa.save()
            return render (request, "MyBus/Principal.html")
    else:
        miFormulario=TarifaFormulario()
    return render (request, "MyBus/tarifa.html", {"miFormulario": miFormulario})

def colectivoApi(request):
    colectivo_todos = Colectivo.objects.all()
    return HttpResponse(serializers.serialize('json',colectivo_todos))

def recorridoApi(request):
    recorrido_todas = Recorrido.objects.all()
    return HttpResponse(serializers.serialize('json',recorrido_todas))

def tarifaApi(request):
    tarifa_todas = Tarifa.objects.all()
    return HttpResponse(serializers.serialize('json',tarifa_todas))