from datetime import date, timedelta
from decimal import Decimal

from django.contrib.auth.models import Group, User
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from .forms import PlatoForm
from .models import Categoria, Ingrediente, Plato


class BaseTest(TestCase):
    def setUp(self):
        call_command('crear_roles')
        self.admin = User.objects.create_user('admin1', password='x12345678')
        self.admin.groups.add(Group.objects.get(name='Administrador'))
        self.mesero = User.objects.create_user('mesero1', password='x12345678')
        self.mesero.groups.add(Group.objects.get(name='Mesero'))

        self.cat = Categoria.objects.create(nombre='Platos fuertes')
        self.queso = Ingrediente.objects.create(nombre='Queso', es_alergeno=True)
        self.plato = Plato.objects.create(
            codigo='LS001', nombre='Lasaña', precio=Decimal('9.50'), categoria=self.cat)
        self.plato.ingredientes.add(self.queso)


class PlatoTests(BaseTest):
    def test_login_requerido(self):
        r = self.client.get(reverse('plato_list'))
        self.assertEqual(r.status_code, 302)

    def test_busqueda_por_ingrediente(self):
        self.client.force_login(self.admin)
        r = self.client.get(reverse('plato_list'), {'pista': 'queso'})
        self.assertContains(r, 'Lasaña')
        r = self.client.get(reverse('plato_list'), {'pista': 'zzz'})
        self.assertNotContains(r, 'Lasaña')

    def test_filtro_categoria_invalida_no_rompe(self):
        self.client.force_login(self.admin)
        r = self.client.get(reverse('plato_list'), {'categoria': 'abc'})
        self.assertEqual(r.status_code, 200)

    def test_crear_plato_con_ingredientes(self):
        self.client.force_login(self.admin)
        r = self.client.post(reverse('plato_create'), {
            'codigo': 'pz002', 'nombre': 'Pizza', 'precio': '8.00', 'disponible': 'on',
            'fecha_registro': '2026-01-10',
            'categoria': self.cat.pk, 'ingredientes': [self.queso.pk]})
        self.assertEqual(r.status_code, 302)
        pizza = Plato.objects.get(nombre='Pizza')
        self.assertEqual(pizza.ingredientes.count(), 1)
        self.assertEqual(pizza.codigo, 'PZ002')

    def test_precio_debe_ser_positivo(self):
        futuro = date.today() + timedelta(days=5)
        f = PlatoForm({'codigo': '!', 'nombre': 'x', 'precio': '0',
                       'fecha_registro': futuro, 'categoria': self.cat.pk})
        self.assertFalse(f.is_valid())
        self.assertIn('precio', f.errors)
        self.assertIn('codigo', f.errors)
        self.assertIn('fecha_registro', f.errors)

    def test_404_en_editar_inexistente(self):
        self.client.force_login(self.admin)
        r = self.client.get(reverse('plato_update', args=[9999]))
        self.assertEqual(r.status_code, 404)


class PermisosTests(BaseTest):
    def test_mesero_no_elimina(self):
        self.client.force_login(self.mesero)
        r = self.client.post(reverse('plato_delete', args=[self.plato.pk]))
        self.assertEqual(r.status_code, 403)
        self.assertTrue(Plato.objects.filter(pk=self.plato.pk).exists())

    def test_mesero_puede_editar(self):
        self.client.force_login(self.mesero)
        r = self.client.get(reverse('plato_update', args=[self.plato.pk]))
        self.assertEqual(r.status_code, 200)

    def test_admin_elimina(self):
        self.client.force_login(self.admin)
        self.client.post(reverse('plato_delete', args=[self.plato.pk]))
        self.assertFalse(Plato.objects.filter(pk=self.plato.pk).exists())


class IngredienteCategoriaTests(BaseTest):
    def test_editar_ingrediente(self):
        self.client.force_login(self.admin)
        r = self.client.post(reverse('ingrediente_update', args=[self.queso.pk]),
                             {'nombre': 'Queso mozzarella', 'es_alergeno': 'on'})
        self.assertEqual(r.status_code, 302)
        self.queso.refresh_from_db()
        self.assertEqual(self.queso.nombre, 'Queso mozzarella')

    def test_eliminar_ingrediente(self):
        self.client.force_login(self.admin)
        self.client.post(reverse('ingrediente_delete', args=[self.queso.pk]))
        self.assertFalse(Ingrediente.objects.filter(pk=self.queso.pk).exists())

    def test_categoria_con_platos_no_se_elimina(self):
        self.client.force_login(self.admin)
        self.client.post(reverse('categoria_delete', args=[self.cat.pk]))
        self.assertTrue(Categoria.objects.filter(pk=self.cat.pk).exists())


class SesionTests(BaseTest):
    def test_logout_muestra_pagina(self):
        self.client.force_login(self.admin)
        r = self.client.post(reverse('logout'))
        self.assertContains(r, 'Sesión cerrada')
