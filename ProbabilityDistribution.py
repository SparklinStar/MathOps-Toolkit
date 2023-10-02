import math

class NormalDistribution:
    def __init__(self, mean, std_dev):
        self.mean = mean
        self.std_dev = std_dev

    def pdf(self, x):
        return (1 / (self.std_dev * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - self.mean) / self.std_dev)**2)
