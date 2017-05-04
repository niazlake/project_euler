from random import randint
from fractions import gcd
from math import *
g = []
def PollardRho(n):
    i = 0
    xi = randint(0,n-1)
    k = 2
    y = xi
    while i < n:
        i = i+1
        xi = ((xi^2)-1)%n
        d = gcd(y-xi,n)
        if d != 1 and d != n:
            g.append(d)
        if i == k:
            y = xi
            k = 2*k
    return sorted(g)
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x in seen:
            continue
        seen.add(x)
        result.append(x)
    return result
ola = 0
uoe =[]
while True:
    ola += 1
    k = int(ola*(ola + 1)/2)
    uoe.append(k)
    if len(unique(PollardRho(k))) > 500:
        print(unique(PollardRho(k)))
        print(len(unique(PollardRho(k))))
        print(k)
        break
print(uoe)
