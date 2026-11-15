# Práctica 03: Tipos de datos
# Autor: Martin Caza

entero = 10
decimal = 2.75
texto = "Seco de pollo"
booleano = False
lista = ["sal", "pimienta", "comino"]
tupla = ("entrada", "plato fuerte", "postre")
conjunto = {"arroz", "fréjol", "arroz"}      # no permite repetidos
diccionario = {"plato": "Locro", "precio": 4.25}

for valor in (entero, decimal, texto, booleano,
              lista, tupla, conjunto, diccionario):
    print(valor, "->", type(valor).__name__)

# Conversión entre tipos
print(int("25") + 5)
print(str(3.5) + " dólares")
print(float("7"))
