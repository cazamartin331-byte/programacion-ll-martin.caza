from django.urls import path

from menu.views.plato_views import (
    plato_create, plato_delete, plato_list, plato_update)

urlpatterns = [
    path('platos/', plato_list, name='plato_list'),
    path('platos/crear/', plato_create, name='plato_create'),
    path('platos/<int:pk>/editar/', plato_update, name='plato_update'),
    path('platos/<int:pk>/eliminar/', plato_delete, name='plato_delete'),
]
