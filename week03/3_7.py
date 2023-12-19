a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
if a > b:
    mod = b
else:
    mod = a
while(mod != 0):
    r = mod
    if a > b:
        mod = a % b
        a = mod
    else:
        mod = b % a
        b = mod
print("最大公约数为：",r,sep='')