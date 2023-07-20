from django.contrib.auth.models import User, Group
from factura.models import Factura, Cliente, Producto, Suministrador
from rest_framework import serializers


class FacturaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Factura
        fields = ['fecha', 'suministrador', 'cliente', 'producto', 'cantidad', 'total']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['cedula', 'nombre', 'apellido', 'email', 'direccion', 'telefono']

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio']

class SuministradorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Suministrador
        fields = ['ruc', 'nombre', 'sucursal']


