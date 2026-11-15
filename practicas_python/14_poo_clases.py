# Práctica 14: POO - clases y objetos
# Autor: Martin Caza


class Plato:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.__precio = precio          # atributo privado (encapsulamiento)
        self.categoria = categoria

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self.__precio = valor

    def aplicar_descuento(self, porcentaje):
        self.__precio -= self.__precio * porcentaje / 100

    def __str__(self):
        return f"{self.nombre} ({self.categoria}) - ${self.__precio:.2f}"


encebollado = Plato("Encebollado", 4.00, "Plato fuerte")
helado = Plato("Helado de paila", 2.50, "Postre")

print(encebollado)
print(helado)

encebollado.aplicar_descuento(10)
print("Con descuento:", encebollado)

encebollado.precio = 5
print("Nuevo precio:", encebollado.precio)

try:
    helado.precio = -1
except ValueError as error:
    print("Error:", error)
