from django.urls import path
from MyBus import views

urlpatterns = [
    path('', views.Principal),
    path('colectivo/', views.colectivo, name='Colectivo'),
    path('recorrido/', views.recorrido, name='Recorrido'),
    path('tarifa/', views.tarifa, name='Tarifa'),
    path('colectivoapi/', views.colectivoApi),
    path('recorridoapi/', views.recorridoApi),
    path('tarifaapi/', views.tarifaApi),
    path('busqueda/', views.busqueda),
    path('buscar/', views.buscar)
    ]   