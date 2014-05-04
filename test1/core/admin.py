from django.contrib import admin
from test1.core.models import Persona, Ciudad
# Register your models here.

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('Municipio', 'Ciudad', 'Provincia')
    search_fields = ('Municipio', 'Ciudad', 'Provincia')
    
admin.site.register(Persona)
admin.site.register(Ciudad, CiudadAdmin)