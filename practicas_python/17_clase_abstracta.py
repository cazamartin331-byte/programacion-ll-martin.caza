# Práctica 17: Clases abstractas
# Autor: Martin Caza
from abc import ABC, abstractmethod


class Comida(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def preparar(self):
        """Cada comida se prepara de forma distinta."""

    @abstractmethod
    def calorias(self):
        ...

    def describir(self):
        return f"{self.nombre}: {self.preparar()} ({self.calorias()} kcal)"


class Sopa(Comida):
    def preparar(self):
        return "se hierven los ingredientes a fuego lento"

    def calorias(self):
        return 180


class Postre(Comida):
    def preparar(self):
        return "se mezcla y se lleva al refrigerador"

    def calorias(self):
        return 320


try:
    Comida("genérica")
except TypeError as error:
    print("No se puede instanciar una clase abstracta:", error)

for comida in (Sopa("Sopa de quinua"), Postre("Flan")):
    print(comida.describir())
