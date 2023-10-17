import math

def prime_number(n, x):
    for i in range(2, x+1):
        if n % i == 0:
            return 0
    return 1



n = int(input("请输入需要判断是否为质数的数："))
x = int(math.sqrt(n))
result = prime_number(n, x)
if result == 1:
    print(n,"是质数",end='')
else:
    print(n,"不是质数",end='')