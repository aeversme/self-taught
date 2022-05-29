class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node

    def pop(self):
        if self.head is None:
            raise IndexError('Cannot pop from an empty stack')
        popped_node = self.head
        self.head = self.head.next_node
        return popped_node.data


# three methods for reversing a string
stack = Stack()
string = "Hello world"

# method one: slice
print(string[::-1])

# method two: reversed
print("".join(reversed(string)))

# method three: stack
for char in string:
    stack.push(char)

reversed_string = ""
for j in range(len(string)):
    reversed_string += stack.pop()
print(reversed_string)
