def square_root(c):
    i = 0
    g = c/2
    while (abs(g * g - c)> 0.00000000001):
        g = (g + c/g)/2
    return g

n = int(input("请输入你想要开平方根的数字："))
x = square_root(n)
print(f"{n}的结果是：{x}")
