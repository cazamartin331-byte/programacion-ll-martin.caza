from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('mesas/', views.mesas_list, name='mesas_list'),
    path('mesas/crear/', views.mesas_create, name='mesas_create'),
    path('mesas/<int:pk>/editar/', views.mesas_update, name='mesas_update'),
    path('mesas/<int:pk>/eliminar/', views.mesas_delete, name='mesas_delete'),

    path('clientes/', views.clientes_list, name='clientes_list'),
    path('clientes/crear/', views.clientes_create, name='clientes_create'),
    path('clientes/<int:pk>/editar/', views.clientes_update, name='clientes_update'),
    path('clientes/<int:pk>/eliminar/', views.clientes_delete, name='clientes_delete'),

    path('reservas/', views.reservas_list, name='reservas_list'),
    path('reservas/crear/', views.reservas_create, name='reservas_create'),
    path('reservas/<int:pk>/editar/', views.reservas_update, name='reservas_update'),
    path('reservas/<int:pk>/eliminar/', views.reservas_delete, name='reservas_delete'),
]
