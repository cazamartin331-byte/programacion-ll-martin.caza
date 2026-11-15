from django.db import models
from django.utils import timezone

from .categoria import Categoria
from .ingrediente import Ingrediente


class Plato(models.Model):
    codigo = models.CharField(max_length=6, unique=True)
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)
    fecha_registro = models.DateField(default=timezone.localdate)
    # PROTECT: no se puede borrar una categoría que tenga platos
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name='platos')
    ingredientes = models.ManyToManyField(
        Ingrediente, related_name='platos', blank=True)

    class Meta:
        app_label = 'menu'
        verbose_name = 'Plato'
        verbose_name_plural = 'Platos'
        ordering = ['categoria__nombre', 'nombre']

    def __str__(self):
        return self.nombre
