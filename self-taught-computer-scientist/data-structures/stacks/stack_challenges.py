from random import randint


# check for balanced parentheses
def check_parentheses(input_string):
    stack = []
    for char in input_string:
        if char == '(':
            stack.append(char)
        if char == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


string1 = "(()()())(())(((())()))(())(()(()))"
print(check_parentheses(string1))


# create a maxstack (opposite of a minstack)
class MaxStack:
    def __init__(self):
        self.main = []
        self.max = []

    def push(self, num):
        if len(self.max) == 0:
            self.max.append(num)
        elif num >= self.max[-1]:
            self.max.append(num)
        else:
            self.max.append(self.max[-1])
        self.main.append(num)

    def pop(self):
        self.main.pop()
        self.max.pop()

    def get_max(self):
        return self.max[-1]


max_stack = MaxStack()
for _ in range(20):
    max_stack.push(randint(1, 50))

print(max_stack.main)
print(max_stack.max)
print(max_stack.get_max())
