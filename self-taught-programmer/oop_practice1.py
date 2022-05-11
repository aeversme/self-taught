class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    def __init__(self, wid, len):
        super().__init__()
        self.width = wid
        self.length = len

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    def __init__(self, wid, len):
        super().__init__()
        self.width = wid
        self.length = len

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

    def change_size(self, num):
        self.width += num
        self.length += num
        print(f"Each side is now {self.width}")


rect1 = Rectangle(4, 7)
sq1 = Square(3, 3)

print(f"rect1 perimeter: {rect1.calculate_perimeter()}")
print(f"sq1 perimeter: {sq1.calculate_perimeter()}")

sq1.change_size(4)
print(f"sq1 perimeter: {sq1.calculate_perimeter()}")

rect1.what_am_i()
sq1.what_am_i()


class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider


class Person:
    def __init__(self, name):
        self.name = name


lone_ranger = Person("Lone Ranger")
tonto = Horse("Tonto", lone_ranger)

print(tonto.rider.name)
