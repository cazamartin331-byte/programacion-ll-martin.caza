# Práctica 08: Ciclo for
# Autor: Martin Caza

menu = ["Sopa", "Arroz con pollo", "Ensalada", "Postre"]

for plato in menu:
    print("-", plato)

print()
for i, plato in enumerate(menu, start=1):
    print(f"{i}. {plato}")

print()
# Tabla del 7
for n in range(1, 11):
    print(f"7 x {n} = {7 * n}")

# Suma de los primeros 10 números
suma = 0
for n in range(1, 11):
    suma += n
print("Suma 1..10:", suma)
