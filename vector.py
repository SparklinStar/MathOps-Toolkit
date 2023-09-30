class Vector:
    def __init__(self, components):
        self.components = components

    def __str__(self):
        return "(" + ", ".join(map(str, self.components)) + ")"

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    def __setitem__(self, index, value):
        self.components[index] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for addition.")
        result_components = [x + y for x, y in zip(self.components, other.components)]
        return Vector(result_components)

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for subtraction.")
        result_components = [x - y for x, y in zip(self.components, other.components)]
        return Vector(result_components)

    def __mul__(self, scalar):
        result_components = [x * scalar for x in self.components]
        return Vector(result_components)

    def dot(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension for dot product.")
        return sum(x * y for x, y in zip(self.components, other.components))

    def cross(self, other):
        if len(self) != 3 or len(other) != 3:
            raise ValueError("Cross product is defined for 3-dimensional vectors only.")
        result_components = [
            self.components[1] * other.components[2] - self.components[2] * other.components[1],
            self.components[2] * other.components[0] - self.components[0] * other.components[2],
            self.components[0] * other.components[1] - self.components[1] * other.components[0]
        ]
        return Vector(result_components)


