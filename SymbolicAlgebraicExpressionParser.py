import sympy as sp

class AlgebraicExpressionParser:
    def __init__(self, expression_str):
        self.expression_str = expression_str
        self.symbols = sp.symbols('x y z')

    def parse(self):
        parsed_expression = sp.sympify(self.expression_str)
        return parsed_expression
