class FibonacciGenerator:
    def __init__(self):
        self.sequence = [0, 1]

    def generate_sequence(self, n):
        while len(self.sequence) < n:
            next_number = self.sequence[-1] + self.sequence[-2]
            self.sequence.append(next_number)
        return self.sequence[:n]
