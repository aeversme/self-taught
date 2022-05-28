from random import randint


def move_zeros(input_list):
    zero_index = 0
    for index, n in enumerate(input_list):
        if n != 0:
            input_list[zero_index] = n
            if zero_index != index:
                input_list[index] = 0
            zero_index += 1
    return input_list


list_with_zeros = [8, 0, 3, 0, 12]
print(move_zeros(list_with_zeros))


# using the zip built-in function to combine lists
movie_list = ["Interstellar", "Inception", "The Prestige", "insomnia", "Batman Begins"]
ratings_list = [1, 10, 10, 8, 6]

print(list(zip(movie_list, ratings_list)))


# checking for duplicates in a list
def return_duplicates(input_list):
    duplicates = []
    item_set = set()

    for item in input_list:
        len1 = len(item_set)
        item_set.add(item)
        len2 = len(item_set)
        if len1 == len2:
            duplicates.append(item)
    return duplicates


list_of_things = ["orange", "banana", "kiwi", "orange", "pineapple", "apple", "kiwi"]
print(return_duplicates(list_of_things))


# finding the intersection of two lists
list_1 = [2, 43, 48, 62, 64, 28, 3]
list_2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]


def return_inter_using_list_comp(list1, list2):
    return [i for i in list1 if i in list2]


print(return_inter_using_list_comp(list_1, list_2))


def return_inter_using_sets(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))


print(return_inter_using_sets(list_1, list_2))


# challenge
"""
Given a list `random_list` of non-negative integers, return a list consisting of all the even elements of 
`random_list`, followed by all the odd elements of `random_list`.
"""
random_list = [randint(1, 100) for _ in range(16)]


def sort_evens_odds(input_list):
    odd_index = 0
    for index, num in enumerate(input_list):
        if num % 2 == 0 and odd_index < index:
            input_list[index], input_list[odd_index] = input_list[odd_index], input_list[index]
            odd_index += 1
        elif num % 2 == 1 and input_list[index - 1] % 2 == 0:
            odd_index = index
    return input_list


print(sort_evens_odds(random_list))
