from django import forms

class ColectivoFormulario(forms.Form):
    linea_colectivo= forms.CharField()
    numero_colectivo= forms.IntegerField()

class RecorridoFormulario(forms.Form):
    linea_colectivo=forms.CharField()
    inicio=forms.CharField()
    destino=forms.CharField()
    minutos_viaje=forms.IntegerField()

class TarifaFormulario(forms.Form):
    linea_colectivo=forms.CharField()
    valor_pasaje=forms.IntegerField()