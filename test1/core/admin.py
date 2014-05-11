from django.contrib import admin
from test1.core.models import *
# Register your models here.

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('Municipio', 'Provincia', 'CP')
    search_fields = ('Municipio', 'Provincia__Provincia', 'CP')

class NombreAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)
    search_fields = ('Nombre',) 

class ApellidoAdmin(admin.ModelAdmin):
    list_display = ('Apellido',)
    search_fields = ('Apellido',)
    
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('Provincia','id')
    search_fields = ('Provincia','id')
    #ordering = ('Provincia') 

    
admin.site.register(Nombre, NombreAdmin)
admin.site.register(Apellido, ApellidoAdmin)
admin.site.register(Persona_Empresa)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(PayPal)
admin.site.register(Transferencia)
admin.site.register(SMS)
admin.site.register(Lugar)
admin.site.register(Tipo_Servicio)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Pago_Empleado)
admin.site.register(Servicio)