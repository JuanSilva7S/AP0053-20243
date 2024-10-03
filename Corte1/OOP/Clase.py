class Cuadrado:
    def __init__(self, valor):
        self.valor = valor

    def calcular_area(self):
        return self.valor ** 2

class SumarRestar:
    def __init__(self):
        self.resultado = 0

    def sumar(self, a, b):
        self.resultado = a + b

    def restar(self, a, b):
        self.resultado = a - b

    def mostrar_resultado(self):
        print("Resultado =", self.resultado)
