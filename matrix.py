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
    
    def __sub__(self,other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions must match for subtraction.")

        result_matrix = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.columns):
                new_row.append(self.matrix[i][j] - other.matrix[i][j])
            result_matrix.append(new_row)

        return Matrix(result_matrix)
    



