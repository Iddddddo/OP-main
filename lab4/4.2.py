d=float(input('Введите точность счёта 0.0...01: '))
d1=d
d2=d

#рекурсия
def rec(l,r,d):
    x=(l+r)/2
    if r-l < d: return x
    y=x**2-2
    if y<0: l=x
    else: r=x
    return rec(l,r,d)
print(rec(0,5,d))

#Цикл
l=0
r=5
x=(l+r)/2
while (r-l)>d1:
    y=x**2-2
    if y<0: l=x
    else: r=x
    x=(l+r)/2
print(x)

#Лёгкий путь, после пары минут размышлений над черновиком и поиском решения
n=str(d2).count('0')
x=2**(1/2)
print(f'{x:.{n}f}')