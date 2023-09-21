def square_root(c):
    i = 0
    g = 0
    for j in range(0, c+1):
        if (j * j > c and g == 0):
            g = j - 1
    while (abs(g * g - c)> 0.0001):
        g += 0.00001
    return g

n = int(input("请输入你想要开平方根的数字："))
x = square_root(n)
print(f"{n}的结果是：{x}")
