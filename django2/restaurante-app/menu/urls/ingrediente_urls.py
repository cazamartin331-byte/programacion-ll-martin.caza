from django.urls import path

from menu.views.ingrediente_views import (
    ingrediente_create, ingrediente_delete, ingrediente_list, ingrediente_update)

urlpatterns = [
    path('ingredientes/', ingrediente_list, name='ingrediente_list'),
    path('ingredientes/crear/', ingrediente_create, name='ingrediente_create'),
    path('ingredientes/<int:pk>/editar/', ingrediente_update, name='ingrediente_update'),
    path('ingredientes/<int:pk>/eliminar/', ingrediente_delete, name='ingrediente_delete'),
]
