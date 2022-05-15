from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = pi * (self.radius ** 2)
        return round(a, 2)


cir1 = Circle(5)
print(cir1.area())
