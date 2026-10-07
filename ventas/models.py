from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100),
    correo = models.TextField(unique=True),
    numero = models.PositiveSmallIntegerField(),

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    cliente = models.ForeignKey(),
    total = models.PositiveBigIntegerField(),