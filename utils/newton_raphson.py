from sympy import symbols, lambdify, diff
import matplotlib.pyplot as plt
import numpy as np

# graficar la funcion y los valores de las variables en cada iteración newton raphson
def graph_newton_raphson(f, result, x_range=None):
  """
  Grafica la funcion y los valores de las variables en cada iteración.

  Parámetros:
    f: función a graficar
    result: lista con los valores de las variables en cada iteración
  """

  # Crear la variable simbólica
  x = symbols('x')

  # Convertir la función a una función de Python
  f = lambdify(x, f)

  # Determinar el rango de x si no se proporciona
  if x_range is None:
    x_min = min(result) - 1
    x_max = max(result) + 1
  else:
    x_min, x_max = x_range

  # Crear el rango de valores de x centrado en las iteraciones
  x_values = np.linspace(x_min, x_max, 500)

  # Crear el rango de valores de y
  y_values = f(x_values)

  # Crear la figura con el nombre de las funciones y el nombre de la grafica
  plt.figure()
  plt.title("Raíces de una función Newton-Raphson")
  plt.xlabel("x")
  plt.ylabel("y")

  # Graficar la función
  plt.plot(x_values, y_values, label="f(x)")

  # Graficar los valores de las variables en cada iteración
  for i, x in enumerate(result):
    y = f(x)
    plt.plot(x, y, 'ro')

  # Agregar las etiquetas
  plt.xlabel("x")
  plt.ylabel("f(x)")

  # Mostrar la leyenda
  plt.legend()

  # Mostrar la gráfica
  plt.show()

# newton raphson
def newton_raphson(f, x0, tol=1e-10):
  """
  Encontrar las raíces de una función utilizando el método de Newton-Raphson.

  Parámetros:
    f: función a la que se le quiere encontrar las raíces
    x0: valor inicial de la variable
  
  Retorna:
    result: lista con los valores de las variables en cada iteración
  """

  # Crear la variable simbólica
  x = symbols('x')

  # Crear la función derivada
  f_prime = diff(f, x)

  # Convertir la función a una función de Python
  f = lambdify(x, f)
  f_prime = lambdify(x, f_prime)

  # Inicializar la variable de la iteración
  x = x0

  # Inicializar la lista de resultados
  result = [x]

  # Iterar hasta que se alcance la tolerancia
  while abs(f(x)) > tol:
    x = x - f(x) / f_prime(x)
    result.append(x)

  return result