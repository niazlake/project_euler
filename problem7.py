import time
start = time.time()
x = 2
list_numb = []
def prost(n):
    i = 2
    j = 0
    while i**2<=n and j != 1:
        if n%i == 0:
            j = 1
        i += 1
    if j == 1:
        return False
    else:
        return True

h = 2
while len(list_numb)<=10000:
    h +=1
    if prost(h) == True:
        list_numb.append(h)

end = time.time() - start
print("time:%s result:%s" % (end, list_numb))