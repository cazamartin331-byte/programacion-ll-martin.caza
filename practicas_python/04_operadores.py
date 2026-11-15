# Práctica 04: Operadores
# Autor: Martin Caza

a, b = 17, 5

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Residuo:", a % b)
print("Potencia:", a ** 2)

# Comparación
print("a > b:", a > b)
print("a == b:", a == b)
print("a != b:", a != b)

# Lógicos
hay_stock = True
es_hora_almuerzo = False
print("Se puede vender almuerzo:", hay_stock and es_hora_almuerzo)
print("Se puede vender algo:", hay_stock or es_hora_almuerzo)
print("No hay stock:", not hay_stock)

# Asignación compuesta
cuenta = 20
cuenta += 5
cuenta *= 2
print("Cuenta final:", cuenta)
