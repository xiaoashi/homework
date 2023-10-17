def select_sort(arr):
    for i in range(len(arr)):
        x = 1
        for j in range(i, len(arr)):
            if arr[j] < arr[x]:
                x = j
        arr[i], arr[x] = arr[x], arr[i]
    return arr
#时间复杂度：设arr的长度为n，可以得到这串代码需要运行n*n次，所以为O(n^2)
#空间复杂度：这串代码只需要一个新变量x就可以用来记录，因此为O(1)