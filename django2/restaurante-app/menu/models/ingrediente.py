from django.db import models


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    es_alergeno = models.BooleanField(default=False)

    class Meta:
        app_label = 'menu'
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
