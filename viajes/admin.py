from django.contrib import admin
from viajes.models import Destino, Paquete


@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ('Pais', 'ciudad')

@admin.register(Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'viaje', 'valor', 'disponible', 'hotel')