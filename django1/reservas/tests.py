from datetime import date, time, timedelta

from django.test import TestCase
from django.urls import reverse

from .forms import ReservaForm
from .models import Cliente, Mesa, Reserva


class ReservasTests(TestCase):
    def setUp(self):
        self.mesa = Mesa.objects.create(numero=1, capacidad=4)
        self.cliente = Cliente.objects.create(nombre='Luis', telefono='0999999999')
        self.manana = date.today() + timedelta(days=1)

    def datos(self, **extra):
        base = {'mesa': self.mesa.pk, 'cliente': self.cliente.pk,
                'fecha': self.manana, 'hora': '19:00', 'personas': 3,
                'estado': 'PENDIENTE'}
        base.update(extra)
        return base

    def test_crear_reserva(self):
        r = self.client.post(reverse('reservas_create'), self.datos())
        self.assertEqual(r.status_code, 302)
        self.assertEqual(Reserva.objects.count(), 1)

    def test_no_supera_capacidad(self):
        self.assertFalse(ReservaForm(self.datos(personas=9)).is_valid())

    def test_fecha_pasada_invalida(self):
        ayer = date.today() - timedelta(days=1)
        self.assertFalse(ReservaForm(self.datos(fecha=ayer)).is_valid())

    def test_filtrar_por_estado(self):
        Reserva.objects.create(mesa=self.mesa, cliente=self.cliente, fecha=self.manana,
                               hora=time(19, 0), personas=2, estado='CANCELADA')
        r = self.client.get(reverse('reservas_list'), {'estado': 'PENDIENTE'})
        self.assertContains(r, 'No hay reservas')
        r = self.client.get(reverse('reservas_list'), {'estado': 'CANCELADA'})
        self.assertContains(r, 'Luis')

    def test_crud_mesa_y_404(self):
        self.client.post(reverse('mesas_update', args=[self.mesa.pk]),
                         {'numero': 1, 'capacidad': 6, 'ubicacion': 'Terraza'})
        self.mesa.refresh_from_db()
        self.assertEqual(self.mesa.capacidad, 6)
        self.assertEqual(self.client.get(reverse('mesas_update', args=[999])).status_code, 404)
        self.client.post(reverse('mesas_delete', args=[self.mesa.pk]))
        self.assertFalse(Mesa.objects.exists())
