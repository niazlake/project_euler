import math
a = list(str(math.factorial(100)))
g = []
for i in a:
    g.append(int(i))
a = sum(g)
print(a)