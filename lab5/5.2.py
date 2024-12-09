def dks(graf, s):
    n=len(graf)
    q=[(0,s)]
    d=[10**9 for i in range(n)]
    d[s]=0
    while len(q)!=0:
        (cost, u) = q.pop(0)
        for v in range(n):
            if d[v]>d[u]+graf[u][v]:
                d[v]=d[u]+graf[u][v]
                q.append((d[v],v))
    return d

def gp(f):
    global d
    n=len(graf)
    path=[f]
    while f!= start:
        for v in range(n):
            if d[v]==d[f]-graf[f][v]:
                path.append(v)
                f=v
    return path[::-1]

with open("lab5/bd.txt", "r", encoding="utf-8") as f:
    text = f.read()
vers=int(len(text.split())**0.5)

a=[[0 for i in range(vers)] for j in range(vers)]

text=text.split()

k=0
for i in range(vers):
    for j in range(vers):
        a[i][j]=int(text[k])
        if a[i][j]==0: a[i][j]=10**9
        k+=1

graf=a

print('''Точки на карте:
1) Трон рэдиант
2) Нижний лес
3) Дневной рошпит
4) Фонтан с лотосами рэдиант
5) Лавка дайр
6) Большой лес рэдиант
7) Торментор рэдиант
8) Тройка рэдиант
9) Тройка дайр
10) Торментор дайр
11) Трон дайр
12) Верхний лес
13) Большой лес дайр
14) Лавка рэдиант
15) Фонтан с лотосами дайр
16) Ночной рошпит''')
start=int(input('Введите точку отправления: '))-1
stop=int(input('Введите пункт назначения: '))-1

d=dks(graf,start)
print('Расстояние: ', d[stop])
print('Маршрут: ', end = '')
for i in range(len(gp(stop))):
    if i!=len(gp(stop))-1:
        print(gp(stop)[i]+1, end=' -> ')
    else: print(gp(stop)[i]+1)