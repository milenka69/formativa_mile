from django.contrib import admin
from viajes.models import Destino, Paquete


@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'descripcion')
    list_filter = ('pais',)
    search_fields = ('nombre', 'pais', 'descripcion')

@admin.register(Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'viaje', 'valor', 'disponible', 'hotel')
    list_filter = ('viaje', 'disponible', 'hotel')
    list_editable = ('disponible', 'hotel')
    search_fields = ('nombre', 'viaje__nombre', 'viaje__pais')