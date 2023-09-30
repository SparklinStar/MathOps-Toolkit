class SetOperations:
    def __init__(self, set1, set2):
        self.set1 = set(set1)
        self.set2 = set(set2)

    def union(self):
        return self.set1.union(self.set2)

    def intersection(self):
        return self.set1.intersection(self.set2)

    def difference(self):
        return self.set1.difference(self.set2)

    def symmetric_difference(self):
        return self.set1.symmetric_difference(self.set2)

    def is_subset(self):
        return self.set1.issubset(self.set2)

    def is_superset(self):
        return self.set1.issuperset(self.set2)

    def complement(self, universe_set):
        universe = set(universe_set)
        return universe.difference(self.set1)


