from django.contrib import admin
from viajes.models import Destino, Paquete


@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'descripcion', 'activo')
    list_filter = ('pais', 'activo')
    search_fields = ('nombre', 'pais', 'descripcion')
    list_editable = ('activo',)

@admin.register(Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'viaje', 'valor_formateado', 'disponible', 'hotel')
    list_filter = ('viaje', 'disponible', 'hotel')
    list_editable = ('disponible', 'hotel')
    search_fields = ('nombre', 'viaje__nombre', 'viaje__pais')

    @admin.display(description='valor', ordering='valor')
    def valor_formateado(self, obj):
        return f"$ {obj.valor:,}".replace(",", ".")