from random import randint

number_list = [8, 4, 9, 6, 5, 1, 3, 7, 2]
bigger_list = [randint(0, 100000) for _ in range(10000)]


def quicksort(a_list, low_index, high_index):
    if low_index < high_index:
        pivot = partition(a_list, low_index, high_index)
        quicksort(a_list, low_index, pivot - 1)
        quicksort(a_list, pivot + 1, high_index)
    return a_list


def partition(a_list, low_index, high_index):
    pivot = a_list[high_index]

    i = low_index - 1

    for j in range(low_index, high_index):
        if a_list[j] <= pivot:
            i += 1
            a_list[i], a_list[j] = a_list[j], a_list[i]
    i += 1
    a_list[i], a_list[high_index] = a_list[high_index], a_list[i]
    return i


print(quicksort(bigger_list, 0, (len(bigger_list) - 1)))
