n = 1
m = 1/(2 * n - 1)
a = 0
a = a + (-1) ** (n + 1) * m
while (m >= 0.000001):
    n += 1
    m = 1/(2 * n - 1)
    a = a + (-1) ** (n + 1) * m
t = a * 4
print(str(round(t, 10)))

