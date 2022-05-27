from random import randint

number_list = [8, 4, 9, 6, 5, 1, 3, 7, 2]
bigger_list = [randint(0, 100000) for _ in range(10000)]


def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        left_index = 0
        right_index = 0
        a_list_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                a_list[a_list_index] = left_half[left_index]
                left_index += 1
            else:
                a_list[a_list_index] = right_half[right_index]
                right_index += 1
            a_list_index += 1

        while left_index < len(left_half):
            a_list[a_list_index] = left_half[left_index]
            left_index += 1
            a_list_index += 1

        while right_index < len(right_half):
            a_list[a_list_index] = right_half[right_index]
            right_index += 1
            a_list_index += 1

    return a_list


print(merge_sort(number_list))
print(merge_sort(bigger_list))
