w = int(input("请输入w的值："))
x = int(input("请输入x的值："))
y = int(input("请输入y的值："))
z = int(input("请输入z的值："))

numbers = [w, x, y, z]

numbers.sort(reverse=True)

for num in numbers:
    print(num,end=" ")