import numpy as np

# Coefficient matrix
A = np.array([[2, 3],
              [4, 5]])

# Constants vector
b = np.array([10, 20])

# Solve the system
try:
    solution = np.linalg.solve(A, b)
    print("Solution (x, y) is:", solution)
except np.linalg.LinAlgError:
    print("The system has no unique solution.")
