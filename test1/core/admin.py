from django.contrib import admin
from test1.core.models import *
# Register your models here.

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('Municipio', 'Ciudad', 'Provincia')
    search_fields = ('Municipio', 'Ciudad', 'Provincia')
    
admin.site.register(Nombre)
admin.site.register(Apellido)
admin.site.register(Persona_Empresa)
admin.site.register(Provincia)
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