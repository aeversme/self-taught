from random import randint

number_list = [8, 4, 9, 6, 5, 1, 3, 7, 2]
bigger_list = [randint(0, 100000) for _ in range(10000)]


def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        value = a_list[i]
        while i > 0 and a_list[i - 1] > value:
            a_list[i] = a_list[i - 1]
            i -= 1
        a_list[i] = value
    return a_list


print(insertion_sort(bigger_list))
