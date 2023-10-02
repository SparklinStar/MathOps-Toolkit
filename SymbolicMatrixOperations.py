import sympy as sp

class SymbolicMatrixOperations:
    def __init__(self, matrix_symbols):
        self.matrix_symbols = matrix_symbols

    def matrix_multiply(self, matrix1, matrix2):
        if matrix1.shape[1] != matrix2.shape[0]:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix.")
        return sp.MatMul(matrix1, matrix2)

    def matrix_transpose(self, matrix):
        return matrix.T

    def matrix_determinant(self, matrix):
        return sp.det(matrix)
