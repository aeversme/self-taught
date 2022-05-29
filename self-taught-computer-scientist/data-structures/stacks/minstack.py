from random import randint


class MinStack:
    def __init__(self):
        self.main = []
        self.min = []

    def push(self, num):
        if len(self.main) == 0:
            self.min.append(num)
        elif num <= self.min[-1]:
            self.min.append(num)
        else:
            self.min.append(self.min[-1])
        self.main.append(num)

    def pop(self):
        self.min.pop()
        return self.main.pop()

    def get_min(self):
        return self.min[-1]


min_stack = MinStack()
for _ in range(20):
    min_stack.push(randint(1, 51))

print(min_stack.main)
print(min_stack.min)
print(min_stack.get_min())
