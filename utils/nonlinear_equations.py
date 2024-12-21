from sympy import symbols, lambdify, diff
import matplotlib.pyplot as plt
import numpy as np

# graficar las funciones y los puntos sistema de ecuaciones no lineales
def graph_nonlinear_equations(f1, f2, result):
  """
  Grafica las funciones y los puntos de una lista de resultados.

  Parámetros:
    f1: función 1
    f2: función 2
    result: lista de los puntos de cada iteracción
  """

  x, y = symbols('x0 x1')  # Variables simbólicas

  # Convertir funciones simbólicas en funciones numéricas
  f1_func = lambdify((x, y), f1, 'numpy')
  f2_func = lambdify((x, y), f2, 'numpy')

  # Crear un grid
  x = np.linspace(-10, 10, 400)
  y = np.linspace(-10, 10, 400)
  X, Y = np.meshgrid(x, y)

  # Calcular los valores de las funciones
  Z1 = f1_func(X, Y)
  Z2 = f2_func(X, Y)

  # Crear la figura con el nombre de las funciones y el nombre de la grafica
  plt.figure()
  plt.title("Sistema de ecuaciones no lineales")
  plt.xlabel("x")
  plt.ylabel("y")

  # Graficar las funciones
  plt.contour(X, Y, Z1, levels=0, colors='r')
  plt.contour(X, Y, Z2, levels=0, colors='b')

  # Graficar los puntos
  x = [x for x, y in result]
  y = [y for x, y in result]
  plt.plot(x, y, 'go-')

  plt.show()

# newton raphson n variables sistema de ecuaciones no lineales
def newton_raphson_n_variables(f, x0, n, iterations):
  """
  Resuelve un sistema de ecuaciones no lineales con n variables utilizando el método de Newton-Raphson.

  Parámetros:
    f: lista de funciones, cada una con n variables
    x0: lista con los valores iniciales para cada variable (longitud n)
    n: número de variables
    iterations: número de iteraciones

  Retorna:
    result: lista con los puntos (valores de las variables) en cada iteración
  """
  # Variables simbólicas
  variables = symbols('x0:%d' % n)

  # Convertir las funciones simbólicas a funciones numéricas
  f_funcs = [lambdify(variables, func, 'numpy') for func in f]

  # Calcular el jacobiano
  jacobian = []
  for func in f:
    jacobian_row = [diff(func, var) for var in variables]
    jacobian.append(jacobian_row)
  
  jacobian_func = lambdify(variables, jacobian, 'numpy')

  # Inicializar la lista de resultados
  result = [tuple(x0)]

  # Método de Newton-Raphson
  for _ in range(iterations):
    # Evaluar el jacobiano y las funciones en el punto actual
    jacobian_val = jacobian_func(*x0)
    f_vals = [f_func(*x0) for f_func in f_funcs]

    # Convertir el jacobiano en una matriz NumPy
    jacobian_matrix = np.array(jacobian_val, dtype=float)
    f_values = np.array(f_vals, dtype=float)

    # Resolver el sistema lineal para calcular los incrementos
    try:
      delta = np.linalg.solve(jacobian_matrix, f_values)
    except np.linalg.LinAlgError:
      print("El jacobiano es singular o no invertible en esta iteración.")
      break

    # Actualizar los valores de las variables
    x0 = x0 - delta

    # Guardar el resultado de la iteración
    result.append(tuple(x0))

  return result
