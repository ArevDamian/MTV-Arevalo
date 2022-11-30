from django.db import models

# Create your models here.
class Colectivo (models.Model):
    linea_colectivo=models.CharField(max_length=40)
    numero_colectivo=models.IntegerField()

class Recorrido (models.Model):
    linea_colectivo=models.CharField(max_length=40)
    inicio=models.CharField(max_length=50)
    destino=models.CharField(max_length=50)
    minutos_viaje=models.IntegerField()

class Tarifa (models.Model):
    linea_colectivo=models.CharField(max_length=40)
    valor_pasaje=models.IntegerField()

    
