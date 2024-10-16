x, n = map(float, input().split())
n=int(n)
s = x
zn = 1
ch = x
for i in range(1,n):
    ch = -(ch * (x ** 2))
    zn += 2
    s += ch/zn
print(s)
