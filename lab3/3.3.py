'''
В списке A=(a1, а2, ..., аn) удалить все положительные элементы, имеющие четный
порядковый номер, идущие после минимального элемента списка
'''
s=input()
a=[]
ans=[]
buf=s.split(', ')
for i in buf:
    a.append(int(i))

st=min(a)
ans=[]
f1=False
for i in range(len(a)):
    if f1 and a[i] > 0 and i%2==1:
        None
    else:
        ans.append(a[i])
    if a[i]==st:
        f1=True
print(str(ans)[1:-1])