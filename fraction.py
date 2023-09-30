import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        common_divisor = math.gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        if not isinstance(other, Fraction):
            raise ValueError("Unsupported operand type for addition.")

        common_denominator = self.denominator * other.denominator
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        return Fraction(new_numerator, common_denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        if not isinstance(other, Fraction):
            raise ValueError("Unsupported operand type for subtraction.")

        common_denominator = self.denominator * other.denominator
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        return Fraction(new_numerator, common_denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        if not isinstance(other, Fraction):
            raise ValueError("Unsupported operand type for multiplication.")

        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)

        if not isinstance(other, Fraction):
            raise ValueError("Unsupported operand type for division.")

        if other.numerator == 0:
            raise ValueError("Division by zero is not allowed.")

        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

