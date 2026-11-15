# Ejercicios del ORM de Django — Reservas

Autor: Martin Caza. Se ejecutan con `python manage.py shell`.

```python
from datetime import date, time
from reservas.models import Mesa, Cliente, Reserva

# Crear
m1 = Mesa.objects.create(numero=1, capacidad=4, ubicacion="Terraza")
m2 = Mesa.objects.create(numero=2, capacidad=2)
c1 = Cliente.objects.create(nombre="Luis Pérez", telefono="0991234567")
Reserva.objects.create(mesa=m1, cliente=c1, fecha=date(2026, 12, 24),
                       hora=time(20, 0), personas=4)

# Leer
Mesa.objects.all()
Mesa.objects.get(numero=1)
Mesa.objects.filter(capacidad__gte=4)
Mesa.objects.exclude(ubicacion="Terraza")
Mesa.objects.order_by("-capacidad")
Cliente.objects.filter(nombre__icontains="pérez").exists()
Mesa.objects.count()

# Relaciones
c1.reservas.all()                  # reservas de un cliente (related_name)
m1.reservas.filter(estado="PENDIENTE")
Reserva.objects.filter(cliente__nombre__startswith="Luis")

# Actualizar
Reserva.objects.filter(cliente=c1).update(estado="CONFIRMADA")

# Agregaciones
from django.db.models import Count, Sum
Mesa.objects.aggregate(total_asientos=Sum("capacidad"))
Cliente.objects.annotate(n=Count("reservas")).order_by("-n")

# Eliminar
Reserva.objects.filter(estado="CANCELADA").delete()
```
