# Bubble Sort
from random import randint
import datetime


number_list = [8, 4, 9, 6, 5, 1, 3, 7, 2]
bigger_list = [randint(0, 100000) for _ in range(10000)]


# written from scratch, before looking at the book solution
def bubble_sort(a_list):
    swap_count = -1
    while swap_count != 0:
        swap_count = 0
        for i in range(len(a_list) - 1):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                swap_count += 1
    return a_list


# book solution
def bubble_sort_book(a_list):
    list_length = len(a_list) - 1
    for i in range(list_length):
        no_swaps = True
        # subtracting i in the second loop's range improves sort efficiency
        for j in range(list_length - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                no_swaps = False
        if no_swaps:
            return a_list
    return a_list


def compare_sorts(input_list):
    input_list_copy = input_list.copy()
    first_start = datetime.datetime.utcnow()
    bubble_sort(input_list)
    first_end = datetime.datetime.now().utcnow()
    print(f"First sort: {(first_end - first_start).total_seconds()} seconds")
    second_start = datetime.datetime.utcnow()
    bubble_sort_book(input_list_copy)
    second_end = datetime.datetime.utcnow()
    print(f"Second sort: {(second_end - second_start).total_seconds()} seconds")
    return None


compare_sorts(bigger_list)

"""
First sort method averages ~7.5 seconds. Second method averages ~4.5 seconds.
"""
