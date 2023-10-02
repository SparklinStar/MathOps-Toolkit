class PrimeGenerator:
    def __init__(self):
        self.primes = []

    def generate_primes(self, n):
        if not self.primes:
            self.primes = [2]
        num = self.primes[-1] + 1
        while len(self.primes) < n:
            for p in self.primes:
                if num % p == 0:
                    break
            else:
                self.primes.append(num)
            num += 1
        return self.primes[:n]
