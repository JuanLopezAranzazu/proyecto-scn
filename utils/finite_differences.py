import numpy as np
import matplotlib.pyplot as plt

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
        
        p = px(xi) / (2 * h)
        q = qx(xi)
        r = rx(xi) * h**2

        # Fill the matrix row by row
        if i > 1:
            A[i - 1, i - 2] = -1 - p
        A[i - 1, i - 1] = 2 + h**2 * q
        if i < n:
            A[i - 1, i] = -1 + p

        # Fill the b vector
        b[i - 1] = r

    # Apply boundary conditions
    b[0] += (1 + px(x1 + h) / (2 * h)) * y1
    b[-1] += (1 - px(x2 - h) / (2 * h)) * y2

    # Solve the system
    y_inner = np.linalg.solve(A, b)

    # Combine the solution with boundary conditions
    y = np.concatenate(([y1], y_inner, [y2]))


    return x, y

# Example Usage
if __name__ == "__main__":

    # ask to user to enter the values of the coefficients
    px = float(input("Enter the value of px: "))
    qx = float(input("Enter the value of qx: "))
    rx = float(input("Enter the value of rx: "))

    # Coefficients of the differential equation
    coefficients = {
        'px': lambda x: px,  # Example: p(x) = 0
        'qx': lambda x: qx,  # Example: q(x) = -2
        'rx': lambda x: rx   # Example: r(x) = 1
    }

    # ask to user to enter the values of the boundary points

    x1 = float(input("Enter the value of x1: "))
    y1 = float(input("Enter the value of y1: "))
    x2 = float(input("Enter the value of x2: "))
    y2 = float(input("Enter the value of y2: "))

    # Boundary points
    points = [(x1, y1), (x2, y2)]


    # Number of discretization points
    n = int(input("Enter the number of discretization points: "))

    # Solve the differential equation
    x, y = solve_finite_differences(coefficients, points, n)

    # Print results
    for xi, yi in zip(x, y):
        print(f"x = {xi:.4f}, y = {yi:.4f}")

    # Plot the results
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Solution')
    plt.title('Finite Differences Solution')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()