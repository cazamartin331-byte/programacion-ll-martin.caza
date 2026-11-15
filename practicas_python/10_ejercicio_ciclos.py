# Práctica 10: Ejercicio de ciclos
# Registra pedidos y calcula el total de la cuenta.
# Autor: Martin Caza

total = 0.0
pedidos = []

while True:
    nombre = input("Plato (o 'fin' para terminar): ").strip()
    if nombre.lower() == "fin":
        break
    precio = float(input(f"Precio de {nombre}: $"))
    pedidos.append((nombre, precio))
    total += precio

print("\n--- CUENTA ---")
for nombre, precio in pedidos:
    print(f"{nombre:<20} ${precio:>6.2f}")
print("-" * 28)
print(f"{'TOTAL':<20} ${total:>6.2f}")

# Patrón de asteriscos
print()
for fila in range(1, 6):
    print("*" * fila)
