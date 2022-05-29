from random import randint


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        node_list = []
        node = self.head
        while node is not None:
            node_list.append(node.data)
            node = node.next_node
        return f"Nodes: {node_list}"

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = Node(data)

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            else:
                current = current.next_node
        return False

    def remove(self, target):
        if self.head == target:
            self.head = self.head.next_node
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.next_node = current.next_node
            previous = current
            current = current.next_node

    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            next_node = current.next_node
            current.next_node = previous
            previous = current
            current = next_node
        self.head = previous

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next_node
                fast = fast.next_node.next_node
                if slow is fast:
                    return True
            except AttributeError:
                return False


random_list = LinkedList()

for i in range(20):
    num = randint(1, 30)
    random_list.append(num)

print(random_list)
print(random_list.search(10))
random_list.remove(10)
print(random_list)
random_list.reverse_list()
print(random_list)
print(random_list.detect_cycle())
