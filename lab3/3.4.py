def chk(j, prims):
    for i in prims:
        if j%i==0:
            return prims
    prims.append(j)
    return prims

n=int(input("Введите n: "))
i=1
while i*7<=n:
    print(i*7, end=', ')
    i += 1
prims=[2,3]
print()
if n>=25:
    for j in range(5, n+1):
        prims=chk(j,prims)
print(str(prims)[1:-1])
