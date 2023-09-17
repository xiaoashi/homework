def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("输入要进行阶乘的数字："))
print(f"{n} 的阶乘是: {factorial(n)}")