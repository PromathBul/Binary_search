from Methods import enter
from Methods import create_list_ascending_order as create
from Methods import binary_search as search

import os

os.system ('cls')

size = enter('Введите размер списка: ')
min_value = enter('Enter the minimum possible value for the first element: ')
max_value = enter('Enter the maximum possible value for the first element: ')


sorted_list = create (min_value, max_value, size)
print (sorted_list)

target = enter('Enter the number whose index you want to find: ')

result = search (sorted_list, target)
print (f'Search result: {result}')