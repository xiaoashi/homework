def cube_root(n):
    left = 0.0
    right = n

    while True:
        mid = (left + right) / 2
        diff = mid ** 3 - n

        if abs(diff) < 0.00001:
            return mid

        if diff > 0:
            right = mid
        else:
            left = mid

number = int(input("输入想要3次方根的数字："))
result = cube_root(number)
print(f"The cube root of {number} is approximately {result}.")