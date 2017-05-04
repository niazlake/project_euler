a = list(range(1,501))
b = list(range(1,501))
c = list(range(1,501))
for i in a:
    for j in b:
        for k in c:
            if i+k+j == 1000 and i<j<k and j**2+i**2==k**2 :
                print(i)
                print(j)
                print(k)
                break
