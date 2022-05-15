class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n


# client: code outside the class that uses an object of that class
data1 = Data()
data1.nums[0] = 100
print(f"data1.nums: {data1.nums}")

data2 = Data()
data2.change_data(0, 100)
print(f"data2.nums: {data2.nums}")


class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._private = "unsafe"

    def public_method(self):
        # clients can use this
        pass

    def _private_method(self):
        # clients shouldn't use this
        pass
