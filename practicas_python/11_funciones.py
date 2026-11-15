# Práctica 11: Funciones
# Autor: Martin Caza


def calcular_iva(valor, porcentaje=15):
    """Devuelve el valor del IVA."""
    return valor * porcentaje / 100


def precio_final(valor, porcentaje=15):
    return valor + calcular_iva(valor, porcentaje)


def es_par(numero):
    return numero % 2 == 0


def promedio(*numeros):
    """Acepta cantidad variable de argumentos."""
    return sum(numeros) / len(numeros)


print("IVA de 20:", calcular_iva(20))
print("Precio final de 20:", precio_final(20))
print("Precio final con IVA 12%:", precio_final(20, porcentaje=12))
print("¿8 es par?", es_par(8))
print("Promedio:", promedio(8, 9, 7.5, 10))
