class ModuloInteger:
    def __init__(self, value, modulus):
        self.value = value % modulus
        self.modulus = modulus

    def __add__(self, other):
        if self.modulus != other.modulus:
            raise ValueError("Moduli must be the same for addition.")
        return ModuloInteger((self.value + other.value) % self.modulus, self.modulus)

    def __sub__(self, other):
        if self.modulus != other.modulus:
            raise ValueError("Moduli must be the same for subtraction.")
        return ModuloInteger((self.value - other.value) % self.modulus, self.modulus)

    def __mul__(self, other):
        if self.modulus != other.modulus:
            raise ValueError("Moduli must be the same for multiplication.")
        return ModuloInteger((self.value * other.value) % self.modulus, self.modulus)

    def __str__(self):
        return str(self.value)
