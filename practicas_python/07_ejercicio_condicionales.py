# Práctica 07: Ejercicio de condicionales
# Calcula el valor a pagar con descuento según el consumo.
# Autor: Martin Caza

consumo = float(input("Valor del consumo: $"))
es_cliente_frecuente = input("¿Cliente frecuente? (s/n): ").lower() == "s"

if consumo <= 0:
    print("El consumo debe ser mayor a 0")
else:
    if consumo >= 50:
        descuento = 0.15
    elif consumo >= 25:
        descuento = 0.10
    else:
        descuento = 0.0

    if es_cliente_frecuente:
        descuento += 0.05

    ahorro = consumo * descuento
    total = consumo - ahorro
    print(f"Descuento aplicado: {descuento * 100:.0f}%")
    print(f"Ahorro: ${ahorro:.2f}")
    print(f"Total a pagar: ${total:.2f}")
