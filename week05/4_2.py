import time
start = time.time()
for n in range(1, 1000001):
    if n % 2 == 0:
        x = 1
end = time.time()
print("")
print('running time: %s seconds'%(end - start))