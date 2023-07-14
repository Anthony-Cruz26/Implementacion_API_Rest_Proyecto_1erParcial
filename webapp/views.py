from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from factura.models import Factura
from rest_framework import viewsets, permissions
from webapp.serializers import UserSerializer

# Create your views here.
def mostrar_facturas(request):
    cantidad_facturas = Factura.objects.count()
    pagina = loader.get_template('facturas.html')
    lista_facturas = Factura.objects.all()
    datos = {'cantidad': cantidad_facturas, 'facturas': lista_facturas}
    return HttpResponse(pagina.render(datos, request))

class UserViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all().order_by('cliente')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


