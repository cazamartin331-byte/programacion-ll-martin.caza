from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

MODELOS = ['categoria', 'ingrediente', 'plato']


class Command(BaseCommand):
    help = 'Crea los grupos Administrador y Mesero con sus permisos.'

    def handle(self, *args, **options):
        admin, _ = Group.objects.get_or_create(name='Administrador')
        mesero, _ = Group.objects.get_or_create(name='Mesero')

        for modelo in MODELOS:
            for accion in ('view', 'add', 'change', 'delete'):
                perm = Permission.objects.get(
                    codename=f'{accion}_{modelo}',
                    content_type__app_label='menu')
                admin.permissions.add(perm)
                # El mesero puede ver, crear y editar, pero no eliminar
                if accion != 'delete':
                    mesero.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS('Grupos creados correctamente.'))
