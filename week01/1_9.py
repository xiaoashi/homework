L = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(L)-1, -1, -1):
    reversed_list.append(L[i])

print(reversed_list)