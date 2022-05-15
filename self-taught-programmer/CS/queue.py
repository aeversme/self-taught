# data structure: queue
# first-in-first-out
import time
import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def simulate_line(self, until_show, max_sale_time):
        """
        :param until_show: int, seconds until show starts & ticket sales end
        :param max_sale_time: int, maximum time it takes to sell one ticket
        :return:
        """
        ticket_line = Queue()
        tickets_sold = []

        for i in range(100):
            ticket_line.enqueue("person" + f"{i}")

        now = time.time()
        t_end = time.time() + until_show

        while now < t_end and not ticket_line.is_empty():
            now = time.time()
            sale_time = random.uniform(0, max_sale_time)
            time.sleep(sale_time)
            person = ticket_line.dequeue()
            tickets_sold.append(person)

        return tickets_sold


queue = Queue()
sold = queue.simulate_line(6, 1)
print(sold)
print(f"{len(sold)} tickets sold!")
