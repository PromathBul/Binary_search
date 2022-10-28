from Methods import create_list_ascending_order as create
from Methods import binary_search as search

from time import time

def simple_search (sorted_list, target):
    for i in sorted_list:
        if target == i:
            return sorted_list.index(i)
    return 'This number isn\'t in the list'

time_binary = []
time_simple = []
time_simple_2 = []

# Размер 10
size = 10
sorted_list = create (0, 5, size)

start = time()
result = search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_binary.append (total_time)

start = time()
result = simple_search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_simple.append (total_time)

# Размер 100

size = 100
sorted_list = create (0, 5, size)

start = time()
result = search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_binary.append (total_time)

start = time()
result = simple_search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_simple.append (total_time)

# Размер 1000

size = 1000
sorted_list = create (0, 5, size)

start = time()
result = search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_binary.append (total_time)

start = time()
result = simple_search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_simple.append (total_time)

# Размер 10000

size = 10000
sorted_list = create (0, 5, size)

start = time()
result = search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_binary.append (total_time)

start = time()
result = simple_search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_simple.append (total_time)

# Размер 100000

size = 100000
sorted_list = create (0, 5, size)

start = time()
result = search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_binary.append (total_time)

start = time()
result = simple_search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_simple.append (total_time)

# Размер 1 000 000

size = 1000000
sorted_list = create (0, 5, size)

start = time()
result = search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_binary.append (total_time)

start = time()
result = simple_search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_simple.append (total_time)

# Размер 10 000 000

size = 10000000
sorted_list = create (0, 5, size)

start = time()
result = search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_binary.append (total_time)

start = time()
result = simple_search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_simple.append (total_time)

# Размер 100 000 000

size = 100000000
sorted_list = create (0, 5, size)

start = time()
result = search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_binary.append (total_time)

start = time()
result = simple_search (sorted_list, sorted_list[-1])
end = time()
total_time = round(((end - start) * 10 ** 3), 2)
time_simple.append (total_time)

print(time_binary)
print(time_simple)