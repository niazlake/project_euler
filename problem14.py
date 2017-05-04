import time

start = time.time()
finish = []
o = []
for i in range(5,1000000):
    print(i)
    while i % 2 == 0:
        i = i/2
        finish.append(i)
    if i == 1:
        o.append(len(finish))
        finish =[]
    elif i%2 != 0:
        i = i*3 +1
        finish.append(i)
print(max(o))
elapsed = (time.time() - start)
print(" %s seconds" % (elapsed))
