# Práctica 05: Condicionales
# Autor: Martin Caza

hora = int(input("Ingresa la hora actual (0-23): "))

if 6 <= hora < 11:
    print("Servimos desayunos")
elif 11 <= hora < 16:
    print("Servimos almuerzos")
elif 16 <= hora < 22:
    print("Servimos meriendas y cenas")
else:
    print("El restaurante está cerrado")
