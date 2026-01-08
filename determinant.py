import numpy as np

# Create a 3x3 matrix (determinant ≠ 0)
matrix = np.array([
    [1, 6, 3],
    [0, 5, 4],
    [5, 6, 8]
])

det = np.linalg.det(matrix)

print("Matrix:")
print(matrix)

print("Determinant:", det)

if det != 0:
    inverse = np.linalg.inv(matrix)
    print("Inverse of the matrix:")
    print(inverse)
else:
    print("Inverse does not exist (determinant is zero)")