from matrix import Matrix
from matrix import MatrixEff
import time

start_vanilla = time.time()
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

result = matrix1 + matrix2
print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Matrix Sum:")
print(result)
end_vanilla = time.time()

start_cython = time.time()
matrix1 = MatrixEff([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = MatrixEff([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

result = matrix1 + matrix2
print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Matrix Sum:")
print(result)
end_cython = time.time()

print(f"Vanilla Python: {end_vanilla - start_vanilla}")
print(f"Cython: {end_cython - start_cython}")

