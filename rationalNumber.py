from fractions import Fraction

class CustomRational:
    def __init__(self, numerator, denominator):
        self.value = Fraction(numerator, denominator)

    def __add__(self, other):
        return CustomRational(self.value.numerator * other.value.denominator + other.value.numerator * self.value.denominator,
                               self.value.denominator * other.value.denominator)

    def __sub__(self, other):
        return CustomRational(self.value.numerator * other.value.denominator - other.value.numerator * self.value.denominator,
                               self.value.denominator * other.value.denominator)

    def __mul__(self, other):
        return CustomRational(self.value.numerator * other.value.numerator,
                               self.value.denominator * other.value.denominator)

    def __truediv__(self, other):
        return CustomRational(self.value.numerator * other.value.denominator,
                               self.value.denominator * other.value.numerator)

    def __str__(self):
        return str(self.value)
