class Square:
    square_list = []

    def __init__(self, len):
        self.length = len
        self.square_list.append(self)

    def __repr__(self):
        return f"{self.length} by {self.length} by {self.length} by {self.length}"


sq1 = Square(4)
sq2 = Square(7)
print(Square.square_list)
