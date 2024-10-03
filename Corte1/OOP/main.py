import Clase

# Creando objeto de la clase Cuadrado
objeto1 = Clase.Cuadrado(5)
print(f"Desde la clase Cuadrado: {objeto1.calcular_area()}")

# Creando objeto de la clase SumarRestar
objeto2 = Clase.SumarRestar()

objeto2.sumar(2, 3)
objeto2.mostrar_resultado()

objeto2.restar(2, 3)
objeto2.mostrar_resultado()
