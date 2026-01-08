Linear Algebra Using Python (NumPy)
- Overview

This repository demonstrates fundamental Linear Algebra operations implemented using Python and NumPy.
The code focuses on matrix-based computation commonly used in Data Science, Machine Learning, and Artificial Intelligence.

The following operations are covered:

Determinant of a matrix

Inverse of a matrix

Solution of a system of linear equations

- Technologies

Python 3

NumPy

Git & GitHub

- Repository Structure
LinearAlgebraPython/
│
├── determinant.py        # Computes determinant and inverse of a 3x3 matrix
├── solve_system.py       # Solves a system of linear equations
└── README.md             # Documentation

- Determinant and Inverse of a Matrix
- Description

A 3×3 matrix is defined using NumPy arrays.

The determinant is calculated using linear algebra methods.

If the determinant is non-zero, the inverse of the matrix is computed.

If the determinant is zero, the inverse does not exist.

- Mathematical Condition

The inverse of a matrix exists only when its determinant is not equal to zero.

- Execution
python determinant.py

- Solving a System of Linear Equations
Given System
2x + 3y = 10  
4x + 5y = 20

- Method Used

The equations are represented in matrix form as Ax = b.

NumPy’s np.linalg.solve() method is used to compute the solution.

- Execution
python solve_system.py

- Output
Solution (x, y) is: [5. 0.]

- NumPy Functions Used
- Function & its Purpose
np.array()	Matrix creation
np.linalg.det()	Determinant calculation
np.linalg.inv()	Matrix inverse
np.linalg.solve()	Linear system solution
- Key Concepts Demonstrated

Matrix representation of equations

Determinant and inverse conditions

Solving linear equations using numerical methods

Practical use of NumPy for linear algebra

- Notes

A matrix inverse exists only when the determinant is non-zero.

Decimal values in the output are expected due to floating-point computation.

The approach can be extended to higher-dimensional systems.
