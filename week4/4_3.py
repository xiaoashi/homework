def insertSort(arr):
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while (preIndex >= 0 ) and (current < arr[preIndex]):
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr

arr = input("请输入你需要排序的数组：")
arr_num = [int(n) for n in arr.split()]
sorted_arr = insertSort(arr_num)
print(sorted_arr)