n = float(input("请输入要转换的数字："))
integer = n // 1
decimal = n - integer
arr = []
size_integer = 0
while(integer != 0):
    arr.append(int(integer % 2))
    size_integer += 1
    integer = integer // 2
size_decimal = size_integer
while(decimal != 0 and (size_decimal - size_integer) < 8):
    arr.append(int(decimal * 2))
    decimal = decimal * 2 - int(decimal * 2)
    size_decimal += 1
print("输出的二进制：",end="")
for n in range(size_integer-1, -1, -1):
    print(arr[n],end='')
print(".",end="")
for n in range(size_integer, size_decimal):
    print(arr[n],end='')