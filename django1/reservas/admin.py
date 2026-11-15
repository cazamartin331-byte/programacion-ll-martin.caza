from django.contrib import admin

from .models import Cliente, Mesa, Reserva

admin.site.register(Mesa)
admin.site.register(Cliente)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'mesa', 'fecha', 'hora', 'personas', 'estado']
    list_filter = ['estado', 'fecha']
