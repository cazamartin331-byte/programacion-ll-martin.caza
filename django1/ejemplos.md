# Ejemplos para evidencia — Django 1 (Reservas)

Autor: Martin Caza

Preparación (una sola vez):

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_datos      # mesas, clientes y reservas de ejemplo
python manage.py createsuperuser   # para /admin/
python manage.py runserver
```

| # | Ejemplo | Cómo correrlo | Qué capturar |
|---|---|---|---|
| 1 | Modelos y migraciones | `python manage.py makemigrations` y `migrate` | Salida de la terminal |
| 2 | Panel de administración | `/admin/` | Lista de reservas |
| 3 | Inicio con contadores | `/` | Página de inicio |
| 4 | CRUD de mesas | `/mesas/` | Lista y formulario |
| 5 | CRUD de clientes | `/clientes/` | Lista con nº de reservas |
| 6 | Reservas con filtro por estado | `/reservas/?estado=PENDIENTE` | Lista filtrada |
| 7 | Validaciones del formulario | `/reservas/crear/` con más personas que la capacidad | Mensaje de error |
| 8 | ORM en el shell | Comandos de `orm_ejercicios.md` | Terminal |
| 9 | Pruebas automáticas | `python manage.py test` | Salida con `OK` |
