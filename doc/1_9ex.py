L = [1, 2, 3, 4, 5]
reversed_list = []
i = len(L) - 1

while i >= 0:
    reversed_list.append(L[i])
    i -= 1

print(reversed_list)