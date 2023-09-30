class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions must match for addition.")

        result_matrix = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.columns):
                new_row.append(self.matrix[i][j] + other.matrix[i][j])
            result_matrix.append(new_row)

        return Matrix(result_matrix)

    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions must match for subtraction.")

        result_matrix = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.columns):
                new_row.append(self.matrix[i][j] - other.matrix[i][j])
            result_matrix.append(new_row)

        return Matrix(result_matrix)

    def scalar_multiply(self, scalar):
        result_matrix = [[scalar * self.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(result_matrix)

    def transpose(self):
        transposed_matrix = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.columns)]
        return Matrix(transposed_matrix)

    def multiply(self, other):
        if self.columns != other.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix.")

        result_matrix = []
        for i in range(self.rows):
            row = []
            for j in range(other.columns):
                dot_product = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.columns))
                row.append(dot_product)
            result_matrix.append(row)

        return Matrix(result_matrix)

    def determinant(self):
        if self.rows != self.columns:
            raise ValueError("Determinant can only be calculated for square matrices.")

        if self.rows == 1:
            return self.matrix[0][0]
        elif self.rows == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            determinant = 0
            for j in range(self.columns):
                submatrix = [row[:j] + row[j + 1:] for row in self.matrix[1:]]
                sign = (-1) ** j
                determinant += sign * self.matrix[0][j] * Matrix(submatrix).determinant()
            return determinant

    def is_invertible(self):
        return self.determinant() != 0

    def inverse(self):
        if not self.is_invertible():
            raise ValueError("Matrix is not invertible.")

        if self.rows == 1:
            return Matrix([[1 / self.matrix[0][0]]])

        cofactor_matrix = [[(-1) ** (i + j) * Matrix(self.matrix[:i] + self.matrix[i + 1:])[:][j].determinant() for j in range(self.columns)] for i in range(self.rows)]
        adjugate = Matrix(cofactor_matrix).transpose()
        determinant = self.determinant()
        return adjugate.scalar_multiply(1 / determinant)

    @staticmethod
    def identity(size):
        return Matrix([[1 if i == j else 0 for j in range(size)] for i in range(size)])
