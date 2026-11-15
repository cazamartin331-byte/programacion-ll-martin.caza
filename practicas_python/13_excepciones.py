# Práctica 13: Excepciones
# Autor: Martin Caza


class PrecioInvalidoError(Exception):
    """Excepción propia para precios no permitidos."""


def validar_precio(precio):
    if precio <= 0:
        raise PrecioInvalidoError("El precio debe ser mayor a 0")
    return precio


def dividir_cuenta(total, personas):
    return total / personas


try:
    print(dividir_cuenta(30, 3))
    print(dividir_cuenta(30, 0))
except ZeroDivisionError:
    print("No se puede dividir entre cero personas")
finally:
    print("Operación terminada")

try:
    numero = int("abc")
except ValueError as error:
    print("Error de conversión:", error)

try:
    validar_precio(-5)
except PrecioInvalidoError as error:
    print("Error:", error)

try:
    with open("archivo_que_no_existe.txt") as f:
        f.read()
except FileNotFoundError:
    print("El archivo no existe")
