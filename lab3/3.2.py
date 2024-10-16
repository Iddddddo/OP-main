'''
В одномерном списке A=(a1, а2, ..., аn) группу элементов, содержащую наибольшее
число подряд идущих отрицательных элементов, переписать в «хвост» списка.
'''
s=input()
a=[]
ans=[]
buf=s.split(', ')
for i in buf:
    a.append(int(i))
last_low=[]
len_low=[]
ll=0
c=0
for i in range(len(a)):
    if a[i] < 0:
        ll = i
        c += 1
    if a[i] >= 0:
        last_low.append(ll)
        len_low.append(c)
        ll = 0
        c = 0
q=max(len_low)
n=0
while len_low[n]!=q:
    n+=1
srez=a[last_low[n]-len_low[n]+1:last_low[n]+1]
osn_srez=a[:last_low[n]-len_low[n]+1]+a[last_low[n]+1:]
ans=str(osn_srez + srez)[1:-1]
print(ans)