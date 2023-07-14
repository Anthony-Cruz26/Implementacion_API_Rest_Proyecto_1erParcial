from django.contrib.auth.models import User, Group
from factura.models import Factura
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Factura
        fields = ['fecha', 'cantidad', 'total']


