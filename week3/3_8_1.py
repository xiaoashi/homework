import random

def generate_random_lists(min_length, max_length, max_value):
    result = []
    for length in range(min_length, max_length):
        random_list = [random.randint(1, max_value)]
        for j in range(1, length):
            random_num = random.randint(0, max_value)
            random_list.append(random_num)
        result.append(random_list)
    return result

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

random_lists = generate_random_lists(5, 10, 100)
print(random_lists)
for lst in random_lists:
    sorted_lst = selection_sort(lst)
    print(sorted_lst)
