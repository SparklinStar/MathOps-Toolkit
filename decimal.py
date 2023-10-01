from decimal import Decimal, getcontext

class CustomDecimal:
    def __init__(self, value):
        getcontext().prec = 28  # Set precision as needed
        self.value = Decimal(value)

    def __add__(self, other):
        return CustomDecimal(self.value + other.value)

    def __sub__(self, other):
        return CustomDecimal(self.value - other.value)

    def __mul__(self, other):
        return CustomDecimal(self.value * other.value)

    def __truediv__(self, other):
        return CustomDecimal(self.value / other.value)

    def __str__(self):
        return str(self.value)
