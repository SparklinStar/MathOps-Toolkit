class Polynomial:
    def __init__(self, coefficients):
        # Remove leading zeros
        while coefficients and coefficients[-1] == 0:
            coefficients.pop()
        self.coefficients = coefficients

    def __str__(self):
        if not self.coefficients:
            return "0"
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef != 0:
                if i == 0:
                    terms.append(str(coef))
                else:
                    if coef == 1:
                        term = f"x^{i}"
                    elif coef == -1:
                        term = f"-x^{i}"
                    else:
                        term = f"{coef}x^{i}"
                    terms.append(term)
        return " + ".join(reversed(terms))

    def degree(self):
        if not self.coefficients:
            return 0
        return len(self.coefficients) - 1

    def evaluate(self, x):
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** i)
        return result

    def __add__(self, other):
        # Pad the shorter polynomial with zeros
        if len(self.coefficients) < len(other.coefficients):
            self.coefficients += [0] * (len(other.coefficients) - len(self.coefficients))
        else:
            other.coefficients += [0] * (len(self.coefficients) - len(other.coefficients))

        result_coeffs = [a + b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(result_coeffs)

    def __sub__(self, other):
        # Pad the shorter polynomial with zeros
        if len(self.coefficients) < len(other.coefficients):
            self.coefficients += [0] * (len(other.coefficients) - len(self.coefficients))
        else:
            other.coefficients += [0] * (len(self.coefficients) - len(other.coefficients))

        result_coeffs = [a - b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(result_coeffs)

    def __mul__(self, other):
        result_coeffs = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                result_coeffs[i + j] += a * b
        return Polynomial(result_coeffs)


