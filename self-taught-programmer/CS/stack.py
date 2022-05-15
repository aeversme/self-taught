# data structure: stack
# last-in-first-out

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


stack = Stack()

# reversing a string
for char in "Hello world":
    stack.push(char)

print(stack.size())

reverse = ""

for i in range(stack.size()):
    reverse += stack.pop()

print(reverse)
