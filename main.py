import sympy as sp
from utils.taylor_polynomial import taylor, absolute_error, relative_error, graph_taylor
from utils.newton_raphson import newton_raphson, graph_newton_raphson

# funcion principal
def main():
  while True:
    print("1. Método polinomio de taylor")
    print("2: Método newton-raphson")
    print("3. Método diferencias finitas")
    print("4. Método sistemas de ecuaciones no lineales (jacobiano)")
    print("5. Método sistema de ecuaciones lineales (jacobi)")
    print("6. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
      # datos de entrada
      f = input("Ingrese la función f(x): ")
      x0 = float(input("Ingrese el punto de aproximación x0: "))
      n = int(input("Ingrese el grado del polinomio de Taylor: "))
      x = float(input("Ingrese el punto en el que se evalúa el error x: "))
      x_range = int(input("Ingrese el rango de x: "))

      # rango de x
      x_range = (x0 - x_range, x0 + x_range)

      # calcular el polinomio de Taylor
      f = sp.sympify(f)
      t = taylor(f, x0, n)
      print(t)

      # imprimir el error absoluto y relativo
      print(f'Error absoluto: {absolute_error(f, t, x)}')
      print(f'Error relativo: {relative_error(f, t, x)}')

      # graficar la función y el polinomio de Taylor
      graph_taylor(f, t, x0, x_range)

    elif option == "2":
         # datos de entrada
      f = input("Ingrese la función f(x): ")
      x0 = float(input("Ingrese el punto de aproximación x0: "))
      tol = float(input("Ingrese la tolerancia: "))
      x_range = int(input("Ingrese el rango de x: "))

      # rango de x
      x_range = (x0 - x_range, x0 + x_range)

      # calcular las raíces de la función
      result = newton_raphson(f, x0, tol)

      # imprimir los resultados
      for i, x in enumerate(result):
        print(f'Raíz {i + 1}: {x}')

      # graficar la función y las raíces
      graph_newton_raphson(f, result, x_range)

    elif option == "3":
      print("Método diferencias finitas")

    elif option == "4":
      print("Método sistemas de ecuaciones no lineales (jacobiano)")

    elif option == "5":
      print("Método sistema de ecuaciones lineales (jacobi)")

    elif option == "6":
      break

    else:
      print("Opción inválida")
  
if __name__ == "__main__":
  # llamar las funciones
  main()
  