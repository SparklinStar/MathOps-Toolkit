class Quaternion:
    def __init__(self, real, imag_i, imag_j, imag_k):
        self.real = real
        self.imag_i = imag_i
        self.imag_j = imag_j
        self.imag_k = imag_k

    def __add__(self, other):
        real = self.real + other.real
        imag_i = self.imag_i + other.imag_i
        imag_j = self.imag_j + other.imag_j
        imag_k = self.imag_k + other.imag_k
        return Quaternion(real, imag_i, imag_j, imag_k)

    def __sub__(self, other):
        real = self.real - other.real
        imag_i = self.imag_i - other.imag_i
        imag_j = self.imag_j - other.imag_j
        imag_k = self.imag_k - other.imag_k
        return Quaternion(real, imag_i, imag_j, imag_k)

    def __mul__(self, other):
        real = (self.real * other.real) - (self.imag_i * other.imag_i) - (self.imag_j * other.imag_j) - (self.imag_k * other.imag_k)
        imag_i = (self.real * other.imag_i) + (self.imag_i * other.real) + (self.imag_j * other.imag_k) - (self.imag_k * other.imag_j)
        imag_j = (self.real * other.imag_j) - (self.imag_i * other.imag_k) + (self.imag_j * other.real) + (self.imag_k * other.imag_i)
        imag_k = (self.real * other.imag_k) + (self.imag_i * other.imag_j) - (self.imag_j * other.imag_i) + (self.imag_k * other.real)
        return Quaternion(real, imag_i, imag_j, imag_k)

    def __str__(self):
        return f"{self.real} + {self.imag_i}i + {self.imag_j}j + {self.imag_k}k"
