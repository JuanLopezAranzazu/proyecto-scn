
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
      print("Método polinomio de taylor")

    elif option == "2":
      print("Método newton-raphson")

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
  