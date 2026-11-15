from django.contrib import admin

from .models import Categoria, Ingrediente, Plato


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'es_alergeno']
    list_filter = ['es_alergeno']
    search_fields = ['nombre']


@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'disponible']
    list_filter = ['categoria', 'disponible']
    search_fields = ['nombre']
    filter_horizontal = ['ingredientes']
