# Ejemplos para evidencia — Django 2 (Menú de restaurante)

Autor: Martin Caza

Preparación (una sola vez):

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_datos      # platos, categorías, ingredientes y usuarios demo
python manage.py runserver
```

Usuarios de demostración (solo para pruebas locales): `admin_demo` y `mesero_demo`,
clave `Demo12345!`.

| # | Ejemplo | Cómo correrlo | Qué capturar |
|---|---|---|---|
| 1 | Modelos en paquetes y migraciones | `python manage.py makemigrations` y `migrate` | Salida de la terminal |
| 2 | Autenticación | `/cuentas/login/` | Pantalla de login |
| 3 | Inicio con contadores | `/` con `admin_demo` | Página de inicio |
| 4 | CRUD de categorías | `/categorias/` | Lista y formulario |
| 5 | CRUD de ingredientes | `/ingredientes/` | Lista |
| 6 | CRUD de platos con búsqueda | `/platos/?pista=queso` | Lista filtrada |
| 7 | Permisos por grupo | Entrar con `mesero_demo` | Lista sin botón Eliminar |
| 8 | Validación de precio | `/platos/crear/` con precio 0 | Mensaje de error |
| 9 | Categoría protegida | Eliminar una categoría con platos | Mensaje de error |
| 10 | Pruebas automáticas | `python manage.py test` | Salida con `OK` |
