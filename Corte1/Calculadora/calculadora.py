class Calculadora:
    def obtener_operandos(self):
        try:
            op1 = float(input("Introduce el primer número: "))
            op2 = float(input("Introduce el segundo número: "))
            return op1, op2
        except ValueError:
            print("Por favor, introduce números válidos.")
            return self.obtener_operandos()

    def sumar(self, op1, op2):
        return op1 + op2

    def restar(self, op1, op2):
        return op1 - op2

    def multiplicar(self, op1, op2):
        return op1 * op2

    def dividir(self, op1, op2):
        if op2 == 0:
            return "Error: No se puede dividir entre 0"
        return op1 / op2

    def imprimir_resultado(self, resultado):
        print(f"Resultado: {resultado}")

    def mostrar_menu(self):
        print("\n¿Qué operación deseas realizar?")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
