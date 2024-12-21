import numpy as np

def jacobi_method(A, b, tol=1e-4, max_iter=100):
  """
  Método de Jacobi para resolver el sistema de ecuaciones Ax = b

  Parámetros:
    A (matrix): Matriz de coeficientes
    b (vector): Vector de términos independientes
    x0 (vector): Aproximación inicial
    tol (float): Tolerancia para el criterio de parada
    max_iter (int): Número máximo de iteraciones

  Retorna:
    list: Lista con las aproximaciones en cada iteración
  """
  A_np = np.array(A, dtype=float)
  b_np = np.array(b, dtype=float)
  n = len(b)
  
  # Empezamos con un vector de ceros como aproximación inicial
  x = np.zeros(n, dtype=float)
  results = [list(x)]  # Guardar el vector inicial

  for k in range(max_iter):
    x_new = np.copy(x)

    for i in range(n):
      sum_ = 0
      for j in range(n):
        if j != i:
          sum_ += A_np[i][j] * x[j]
      x_new[i] = (b_np[i] - sum_) / A_np[i][i]

    # Guardar los valores de esta iteración
    results.append(list(x_new))

    # Comprobamos la convergencia
    if np.linalg.norm(x_new - x, ord=np.inf) < tol:
      return results  # Retornamos las aproximaciones

    x = np.copy(x_new)

  print("El método no convergió en el número máximo de iteraciones.")

  return results
