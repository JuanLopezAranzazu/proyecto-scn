import numpy as np
import matplotlib.pyplot as plt

def graph_finite_differences(result):
  """
  Grafica la solución de una ecuación diferencial utilizando el método de diferencias finitas.

  Parámetros:
    result (tuple): Tupla que contiene los arreglos x y y.
  """
  x, y = result

  plt.plot(x, y, 'o-')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('Solución de la ecuación diferencial')
  plt.grid(True)
  plt.show()

def solve_finite_differences(coefficients, points, n):
    """
    Solves a differential equation using the finite differences method.

    Parameters:
        coefficients (dict): Dictionary containing 'px', 'qx', 'rx' functions.
        points (list of tuples): List of tuples [(x1, y1), (x2, y2)] indicating boundary points.
        n (int): Number of iterations (discretization points).

    Returns:
        x (ndarray): Array of x values.
        y (ndarray): Array of y values.
    """
    # Extract coefficients
    px = coefficients['px']
    qx = coefficients['qx']
    rx = coefficients['rx']

    # Unpack boundary points
    (x1, y1), (x2, y2) = points

    # Step size
    h = (x2 - x1) / (n + 1)

    # Discretize x values
    x = np.linspace(x1, x2, n + 2)

    # Initialize matrices
    A = np.zeros((n, n))
    b = np.zeros(n)

    # Fill the matrix A and vector b
    for i in range(1, n + 1):
        xi = x1 + i * h
        
        p = px(xi)
        q = qx(xi)
        r = rx(xi)

        # Fill the matrix row by row
        if i > 1:
            A[i - 1, i - 2] = 1 + (h / 2) * p # sub-diagonal
        A[i - 1, i - 1] = -2 - h**2 * q # diagonal
        if i < n:
            A[i - 1, i] = 1 - (h / 2) * p # upper-diagonal

        # Fill the b vector
        b[i-1]= r*h**2*x[i]

    # Apply boundary conditions
    b[0] = r * h**2 * x[1] - (1 + h/2*p) * y1
    b[-1] = r * h**2 * x[-2] - (1 - h/2*p) * y2

    # Solve the system
    y_inner = np.linalg.solve(A, b)

    # Combine the solution with boundary conditions
    y = np.concatenate(([y1], y_inner, [y2]))


    return x, y
