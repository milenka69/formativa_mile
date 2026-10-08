from django.db import models

class Destino(models.Model):
    ciudad = models.CharField(max_length=120),
    Pais = models.CharField(max_length=120),

    def __str__(self):
        return self.Pais


class Paquete(models.Model):
    nombre = models.CharField(max_length=100),
    viaje = models.ForeignKey(
        Destino,
        on_delete=models.PROTECT,
        related_name='Paquetes',
    ),
    hotel = models.BooleanField(default=True),
    valor = models.PositiveBigIntegerField(),
    disponible = models.BooleanField(default=True),

    def __str__(self):
        return self.nombre