from decimal import Decimal

from django.contrib.auth.models import Group, User
from django.core.management import call_command
from django.core.management.base import BaseCommand

from menu.models import Categoria, Ingrediente, Plato

CATEGORIAS = ['Entradas', 'Platos fuertes', 'Postres', 'Bebidas']
INGREDIENTES = [('Queso', True), ('Camarón', True), ('Pollo', False),
                ('Arroz', False), ('Maíz', False), ('Cebolla', False),
                ('Leche', True), ('Naranjilla', False)]
PLATOS = [
    ('CE001', 'Ceviche de camarón', '6.50', 'Entradas', ['Camarón', 'Cebolla']),
    ('EM002', 'Empanadas de queso', '3.00', 'Entradas', ['Queso', 'Maíz']),
    ('AR003', 'Arroz con pollo', '5.50', 'Platos fuertes', ['Arroz', 'Pollo', 'Cebolla']),
    ('HE004', 'Helado de paila', '2.50', 'Postres', ['Leche']),
    ('JU005', 'Jugo de naranjilla', '1.75', 'Bebidas', ['Naranjilla']),
]
# Usuarios de demostración (solo para pruebas locales)
USUARIOS = [('admin_demo', 'Administrador'), ('mesero_demo', 'Mesero')]
CLAVE_DEMO = 'Demo12345!'


class Command(BaseCommand):
    help = 'Carga datos de ejemplo y usuarios de demostración.'

    def handle(self, *args, **options):
        call_command('crear_roles')

        cats = {n: Categoria.objects.get_or_create(nombre=n)[0] for n in CATEGORIAS}
        ings = {n: Ingrediente.objects.get_or_create(
            nombre=n, defaults={'es_alergeno': a})[0] for n, a in INGREDIENTES}
        for codigo, nombre, precio, cat, ingredientes in PLATOS:
            plato, _ = Plato.objects.get_or_create(
                nombre=nombre,
                defaults={'codigo': codigo, 'precio': Decimal(precio),
                          'categoria': cats[cat]})
            plato.ingredientes.set([ings[i] for i in ingredientes])

        for usuario, grupo in USUARIOS:
            u, creado = User.objects.get_or_create(username=usuario)
            if creado:
                u.set_password(CLAVE_DEMO)
                u.save()
            u.groups.add(Group.objects.get(name=grupo))

        self.stdout.write(self.style.SUCCESS(
            f'Datos cargados. Usuarios demo: admin_demo y mesero_demo (clave: {CLAVE_DEMO})'))
