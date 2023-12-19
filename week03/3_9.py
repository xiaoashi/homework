def construct_array(A):
    n = len(A)
    left = [1] * n
    right = [1] * n
    for i in range(1, n):
        left[i] = left[i-1] * A[i-1]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * A[i+1]
    B = [left[i] * right[i] for i in range(n)]
    return B

A = [0, 1, 2, 3, 4]
B = construct_array(A)
print(B)