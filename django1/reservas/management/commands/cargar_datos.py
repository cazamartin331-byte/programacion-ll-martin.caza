from datetime import time, timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from reservas.models import Cliente, Mesa, Reserva


class Command(BaseCommand):
    help = 'Carga datos de ejemplo (mesas, clientes y reservas) para las pruebas.'

    def handle(self, *args, **options):
        mesas = [
            Mesa.objects.get_or_create(numero=n, defaults={'capacidad': c, 'ubicacion': u})[0]
            for n, c, u in [(1, 2, 'Salón'), (2, 4, 'Terraza'), (3, 6, 'Salón privado')]
        ]
        clientes = [
            Cliente.objects.get_or_create(nombre=n, defaults={'telefono': t})[0]
            for n, t in [('Luis Pérez', '0991234567'), ('Ana Torres', '0987654321')]
        ]
        hoy = timezone.localdate()
        if not Reserva.objects.exists():
            Reserva.objects.create(mesa=mesas[1], cliente=clientes[0],
                                   fecha=hoy + timedelta(days=1), hora=time(19, 30),
                                   personas=4, estado='CONFIRMADA')
            Reserva.objects.create(mesa=mesas[0], cliente=clientes[1],
                                   fecha=hoy + timedelta(days=2), hora=time(13, 0),
                                   personas=2)
        self.stdout.write(self.style.SUCCESS('Datos de ejemplo cargados.'))
