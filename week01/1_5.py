x = int(input("请输入x的值："))
y = int(input("请输入y的值："))
z = int(input("请输入z的值："))

sorted_nums = sorted([x, y, z])

for num in sorted_nums:
    print(num, end=" ")