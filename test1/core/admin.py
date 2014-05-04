from django.contrib import admin
from test1.core.models import *
# Register your models here.

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('Municipio', 'Ciudad', 'Provincia')
    search_fields = ('Municipio', 'Ciudad', 'Provincia')
    
admin.site.register(Nombre)
admin.site.register(Apellido)
admin.site.register(Persona)
admin.site.register(Provincia)
admin.site.register(Ciudad, CiudadAdmin)