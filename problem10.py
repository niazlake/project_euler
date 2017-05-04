g = list(range(3,2000001))

def prost(n):
    i = 2
    j = 0
    while i**2<=n and j != 1:
        if n%i == 0:
            j = 1
        i += 1
    if j == 1:
        return False
    return True
o = []
for i in g:
    if prost(i) == True:
        o.append(i)
        print(o)