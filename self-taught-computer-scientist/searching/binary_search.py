from bisect import bisect_left

number_list = [10, 12, 13, 14, 15, 18, 19]


def binary_search(num_list, target):
    first = 0
    last = len(num_list) - 1
    while last >= first:
        middle = (first + last) // 2
        if target == num_list[middle]:
            return True
        else:
            if target < num_list[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return False


print(binary_search(number_list, 11))
print(binary_search(number_list, 19))

# the built-in `bisect_left` method returns the index of the target element if it is in the sorted list
# it returns the index where the element should be if it is not in the sorted list
print(bisect_left(number_list, 18))  # returns 5
print(bisect_left(number_list, 20))  # returns 7


# binary search with bisect_left
def bl_binary_search(num_list, target):
    index = bisect_left(num_list, target)
    if index <= len(num_list) and target == num_list[index]:
        return True
    return False


print(bl_binary_search(number_list, 12))
print(bl_binary_search(number_list, 16))


"""
Binary search take O(log n) time.

Binary search only works for SORTED data.
"""
