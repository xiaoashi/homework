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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while left:
        result.append(left[0])
        left = left[1:]

    while right:
        result.append(right[0])
        right = right[1:]

    return result


random_lists = generate_random_lists(5, 10, 100)
print(random_lists)

sorted_lists = []

for lst in random_lists:
    sorted_lst = merge_sort(lst)
    print(sorted_lst)