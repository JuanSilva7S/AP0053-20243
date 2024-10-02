from calculadora import Calculadora

def main():
    calculadora = Calculadora()
    
    while True:
        calculadora.mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "5":
            print("¡Gracias por usar la calculadora! Adiós.")
            break

        if opcion in ["1", "2", "3", "4"]:
            op1, op2 = calculadora.obtener_operandos()

            if opcion == "1":
                resultado = calculadora.sumar(op1, op2)
            elif opcion == "2":
                resultado = calculadora.restar(op1, op2)
            elif opcion == "3":
                resultado = calculadora.multiplicar(op1, op2)
            elif opcion == "4":
                resultado = calculadora.dividir(op1, op2)

            calculadora.imprimir_resultado(resultado)
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")

if __name__ == "__main__":
    main()
