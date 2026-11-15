from django.db import models


class Mesa(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    capacidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=50, default='Salón')

    class Meta:
        ordering = ['numero']

    def __str__(self):
        return f'Mesa {self.numero} ({self.capacidad} personas)'


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        CONFIRMADA = 'CONFIRMADA', 'Confirmada'
        CANCELADA = 'CANCELADA', 'Cancelada'

    # Uno a muchos: una mesa y un cliente pueden tener muchas reservas
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='reservas')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField()
    hora = models.TimeField()
    personas = models.PositiveIntegerField()
    estado = models.CharField(
        max_length=12, choices=Estado.choices, default=Estado.PENDIENTE)

    class Meta:
        ordering = ['fecha', 'hora']

    def __str__(self):
        return f'{self.cliente} - {self.mesa} - {self.fecha} {self.hora}'
