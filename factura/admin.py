from django.contrib import admin

from .models import Factura, Cliente, Producto, Suministrador
# Register your models here.

admin.site.register(Factura)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Suministrador)