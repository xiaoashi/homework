def print_result(n):
    if n == 1 or n == 2:
        print("所求结论是：",n)
    else:
        q = n // 3
        r = n % 3
        if r == 0:
            print("所求正整数列是由",q,"个3组成",sep="")
        elif r == 1:
            print("所求正整数列是由",q-1,"个3和2个2组成",sep="")
        else:
            print("所求正整数列是由",q,"个3和1个2组成",sep="")
    return

n = int(input("请输入一个整数："))
print_result(n)
