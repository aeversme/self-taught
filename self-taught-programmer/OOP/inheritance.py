class Shape:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def print_size(self):
        print("{} by {}".format(self.width, self.length))


# Square inherits Shape's variables and methods
class Square(Shape):
    def area(self):
        return self.width * self.length

    # method overriding
    def print_size(self):
        print("I am {} by {}".format(self.width, self.length))


my_shape = Shape(20, 25)
my_shape.print_size()

a_square = Square(20, 20)
a_square.print_size()
print(f"area: {a_square.area()}")
