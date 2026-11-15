# Práctica 15: POO - herencia
# Autor: Martin Caza


class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base

    def presentarse(self):
        return f"Soy {self.nombre}, trabajo en el restaurante"


class Mesero(Empleado):
    def __init__(self, nombre, sueldo_base, propinas):
        super().__init__(nombre, sueldo_base)
        self.propinas = propinas

    def calcular_sueldo(self):
        return self.sueldo_base + self.propinas


class Cocinero(Empleado):
    def __init__(self, nombre, sueldo_base, especialidad):
        super().__init__(nombre, sueldo_base)
        self.especialidad = especialidad

    def presentarse(self):
        return f"{super().presentarse()}, soy cocinero de {self.especialidad}"


mesero = Mesero("Carlos", 460, 120)
cocinero = Cocinero("Ana", 600, "comida costeña")

print(mesero.presentarse(), "| Sueldo:", mesero.calcular_sueldo())
print(cocinero.presentarse(), "| Sueldo:", cocinero.calcular_sueldo())
print(isinstance(mesero, Empleado), issubclass(Cocinero, Empleado))
