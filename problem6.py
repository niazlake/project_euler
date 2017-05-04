import time

start = time.time()
g = list(range(1,101))
first = 0
for i in g:
    first += i**2
second = (sum(g))**2
result = second-first
end = time.time() - start
print("time:%s result:%s"%(end,result))