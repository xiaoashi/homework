import math
import random

def monte_carlo_integration(f, a, b, num_samples):
    total = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        total += f(x)
    avg = total / num_samples
    result = avg * (b - a)
    return result

def f(x):
    return x ** 2 + 4 * x * math.sin(math.radians(x))

a = 2
b = 3
num_samples = 10000000

integral = monte_carlo_integration(f, a, b, num_samples)
print("定积分的估计值：", integral)