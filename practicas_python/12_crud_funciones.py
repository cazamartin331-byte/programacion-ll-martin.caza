# Práctica 12: CRUD con funciones (menú de platos en memoria)
# Autor: Martin Caza

platos = {}   # {nombre: precio}


def crear():
    nombre = input("Nombre del plato: ").strip()
    if nombre in platos:
        print("Ese plato ya existe")
        return
    platos[nombre] = float(input("Precio: $"))
    print("Plato creado")


def listar():
    if not platos:
        print("No hay platos registrados")
        return
    for nombre, precio in platos.items():
        print(f"- {nombre}: ${precio:.2f}")


def actualizar():
    nombre = input("Plato a actualizar: ").strip()
    if nombre not in platos:
        print("No existe ese plato")
        return
    platos[nombre] = float(input("Nuevo precio: $"))
    print("Plato actualizado")


def eliminar():
    nombre = input("Plato a eliminar: ").strip()
    if platos.pop(nombre, None) is None:
        print("No existe ese plato")
    else:
        print("Plato eliminado")


def menu():
    opciones = {"1": crear, "2": listar, "3": actualizar, "4": eliminar}
    while True:
        print("\n1) Crear  2) Listar  3) Actualizar  4) Eliminar  5) Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "5":
            print("Hasta luego")
            break
        accion = opciones.get(opcion)
        if accion:
            try:
                accion()
            except ValueError:
                print("Precio inválido, intenta de nuevo")
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu()
