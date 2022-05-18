from random import randint

number_list = []
for i in range(20):
    number_list.append(randint(0, 101))
print(number_list)


def is_target_in_list(target, num_list):
    for num in num_list:
        if target == num:
            return True
    return False


print(is_target_in_list(13, number_list))

# using Python's built-in `in` keyword
print(45 in number_list)

"""
Linear search time complexity is O(n); best case is O(1); average is n/2.

Consider using when data is UNSORTED.
"""
