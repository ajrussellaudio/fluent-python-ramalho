from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
