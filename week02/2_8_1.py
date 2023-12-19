import random


def throw_needle(num):
    in_circle = 0
    for n in range(1,num + 1):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            in_circle += 1
    return 4 * in_circle/num

needle = 9999999
result = throw_needle(needle)
print(str(round(result, 10)))