class Rectangle:
    """
    `recs` is a class variable, accessed using the class object. It can share data between instance objects without
    needing a global variable.
    """
    recs = []

    def __init__(self, wid, len):
        # these are instance variables, accessed using the instance object
        self.width = wid
        self.length = len
        self.recs.append((self.width, self.length))

    def print_size(self):
        print("{} by {}".format(self.width, self.length))


r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)

same_r1 = r1
print(r1 is same_r1)
print(r1 is r2)
