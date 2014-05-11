from django.contrib import admin
from test1.core.models import *
# Register your models here.

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('Municipio', 'Ciudad', 'Provincia')
    search_fields = ('Municipio', 'Ciudad', 'Provincia')

class NombreAdmin(admin.ModelAdmin):
    ordering = ('Nombre')  

class ApellidoAdmin(admin.ModelAdmin):
    ordering = ('Apellido')  

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'Provincia')
    search_fields = ('id', 'Provincia')
    #ordering = ('Provincia') 

    
admin.site.register(Nombre)
admin.site.register(Apellido)
admin.site.register(Persona_Empresa)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(PayPal)
admin.site.register(Transferencia)
admin.site.register(SMS)
admin.site.register(Lugar)
admin.site.register(Tipo_Servicio)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Pago_Empleado)
admin.site.register(Servicio)