from random import randint

def enter (message):
    num = int(input(message))
    return num

def create_list_ascending_order (min_value, max_value, size):
    sorted_list = []
    for i in range (size):
        value = randint (min_value, max_value)
        sorted_list.append(value)
        max_value += value - min_value + 1
        min_value = value + 1
    return sorted_list

def binary_search (any_sorted_list, target):
    left = 0
    right = len(any_sorted_list) - 1
    while (left <= right):
        middle = (left + right) // 2
        if any_sorted_list[middle] > target:
            right = middle - 1
        elif any_sorted_list[middle] < target:
            left = middle + 1
        else:
            return middle
    return 'This number isn\'t in the list'