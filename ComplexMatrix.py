class ComplexMatrix:
    def __init__(self, rows):
        self.rows = rows

    def __add__(self, other):
        result = [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.rows, other.rows)]
        return ComplexMatrix(result)

    def __sub__(self, other):
        result = [[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(self.rows, other.rows)]
        return ComplexMatrix(result)

    def __mul__(self, scalar):
        result = [[a * scalar for a in row] for row in self.rows]
        return ComplexMatrix(result)

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.rows])
