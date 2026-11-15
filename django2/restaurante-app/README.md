# Menú de Restaurante — Programación II

**Autor:** Martin Caza
**Institución:** Universidad Tecnológica Equinoccial (UTE)

Aplicación web hecha con Django para administrar el menú de un restaurante:
platos, categorías e ingredientes, con autenticación y permisos por rol.

## Funcionalidades
- CRUD de platos, categorías e ingredientes (vistas basadas en funciones).
- Relación uno a muchos (Plato → Categoría) y muchos a muchos (Plato ↔ Ingrediente).
- Búsqueda por nombre, ingrediente o categoría, y filtro por categoría.
- Login/logout y permisos por grupo (`Administrador` y `Mesero`).
- El mesero puede ver, crear y editar; solo el administrador elimina.
- No se puede eliminar una categoría que tenga platos.
- Validaciones: código del plato (4 a 6 letras o números, único), precio mayor a 0,
  fecha de registro no futura y nombres no vacíos.

## Cómo ejecutarlo
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # opcional; sin DB_NAME usa SQLite
python manage.py migrate
python manage.py crear_roles
python manage.py createsuperuser
python manage.py runserver
```
Abre `http://127.0.0.1:8000/`. Para asignar roles, crea usuarios en `/admin/`
y agrégalos al grupo `Administrador` o `Mesero`.

## Pruebas
```bash
python manage.py test
```

## Estructura
- `config/` — configuración del proyecto.
- `menu/models/` — paquete con Categoria, Ingrediente y Plato.
- `menu/forms/` — paquete de formularios y validaciones.
- `menu/views/` — paquete de vistas con permisos.
- `menu/urls/` — paquete de rutas por entidad.
- `menu/templates/` — plantillas con `base.html`.
- `practicas_python/` — prácticas de Python (variables, ciclos, funciones, excepciones, POO).

## Datos de ejemplo y evidencias
```bash
python manage.py cargar_datos
```
Carga platos, categorías, ingredientes y los usuarios demo `admin_demo` y
`mesero_demo` (clave `Demo12345!`, solo para pruebas locales). La lista de
ejemplos para las evidencias está en `ejemplos.md`.
