x, n = map(float, input().split())
n=int(n)
y = x
f=0
for n in range(1,n):
    if f == 0:
        y -= (x ** (2 * n + 1)) / (2 * n + 1)
        f = 1
    else:
        y += (x ** (2 * n + 1)) / (2 * n + 1)
        f = 0
print(y)

'''
2-8/3+32/5-128/7
'''