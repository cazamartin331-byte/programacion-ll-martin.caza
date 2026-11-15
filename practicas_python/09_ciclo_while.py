# Práctica 09: Ciclo while
# Autor: Martin Caza

# Cuenta regresiva
contador = 5
while contador > 0:
    print(contador)
    contador -= 1
print("¡Listo!")

# Validación de entrada: repetir hasta que sea válida
mesas = 0
while mesas < 1 or mesas > 20:
    mesas = int(input("¿Cuántas mesas hay ocupadas? (1-20): "))
print("Mesas ocupadas:", mesas)

# break y continue
numero = 0
while True:
    numero += 1
    if numero % 2 == 0:
        continue          # salta los pares
    if numero > 9:
        break             # termina el ciclo
    print("Impar:", numero)
