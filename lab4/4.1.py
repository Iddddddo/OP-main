'''
4. Задан граф в виде количества вершин n<=7, количества ребер k<=28 и матрицы инцидентности.
а) Для каждой вершины напечатать список инцидентных ей ребер.
б) Определить степень каждой вершины графа.
в) Проверить, есть ли вершины со степенью 0.
г) Определить число вершин, инцидентных только одному ребру.
д) Определить наибольшее число смежных между собой ребер, инцидентных одной и той же вершине.
е) Проверить, есть ли в графе петли.
'''

import time, random

def rep(graf, n):
    for i in range(n):
        for j in range(n):
            graf[i][j]=max(graf[i][j],graf[j][i])
            graf[i][j]=max(graf[i][j],graf[j][i])
    return graf

n, k = map(int, input('Введите n и k: ').split())

"""
Ввод графа
"""
print("Выберите способ ввода графа:\n1) Матрица смежности\n2) Описание связей для каждой вершины\n3) Рандомно сгенерировать")
var_input=int(input("Вариант "))
graf=[]
if var_input==1:
    print("Вводите каждую строку матрицы смежности, разделяя числа запятой без пробелов:")
    for i in range(n):
        a=input().split(',')
        graf.append(a)
    time.sleep(1)
elif var_input==2:
    print("Поочередно введите в строку через пробел с вершинами под каким номером имеет связь каждая вершина, \nесли связей несколько - введите номер вершины несколько раз, \nесли связь петля - то введите тот же номер вершины")
    for i in range(1,n+1):
        print(f'Введите связи для вершины №{i}: ', end='')
        a=input().split()
        graf_matr=[0 for i in range(n)]
        for j in a:
            graf_matr[int(j)-1]+=1
        graf.append(graf_matr)
        time.sleep(0.5)
else:
    print('Граф будет сгенерирован автоматически')
    graf=[[0 for i in range(n)]for j in range(n)]
    max_connect=max(k//(2*n), 1)
    count=0
    for i in range(n):
        for j in range(n):
            a=random.randint(0,max_connect)
            if count+a<=k and j>=i:
                count+=a
                graf[i][j]=a
            elif count+a>k and count<k and j>=i:
                graf[i][j]=k-count
                count=k
    graf=rep(graf, n)
    while count<k:
        a=random.randint(0,n-1)
        b=random.randint(0,n-1)
        if b>=a:
            graf[a][b]+=1
            count+=1
graf=rep(graf, n)

#Вывод
print("Ваша матрица смежности:")
for x in graf:
    print(x)

#Ребра
edge_1=[]#В i-ой ячейке одна часть ребра
edge_2=[]#В i-ой ячейке вторая часть ребра
for i in range(n):
    for j in range(n):
        if graf[i][j]!=0:
            for k in range(graf[i][j]):
                edge_1.append(i)
                edge_2.append(j)
                edge_1.append(j)
                edge_2.append(i)

#Задание 1
print("\n------------------------\n")
print("Ответ на первое задание:")
four=0
for i in range(n):
    exes=[]
    vers=i+1
    print(f"Инцедентные ребра для вершины {vers}: ", end='')
    s=[]
    for j in range(len(edge_1)):
        if edge_1[j]==i and edge_2[j] not in exes:
            print(edge_2[j]+1, end=' ')
            s.append(edge_2[j]+1)
            exes.append(edge_2[j])
    if len(s)==1:
        four+=1 #Счётчик для четвертого задания
    print()
time.sleep(0.5)

#Задание 2
print("\n------------------------\n")
print("Ответ на второе задание:")
zer=False
inces=[[] for i in range(n)]

for i in range(n): #Тус создаю список длины n, в i-ой ячейке лежат вершины, с которыми имеет связь i-ая вершина
    for j in range(len(edge_1)):
        if edge_1[j]==i:
            inces[i].append(edge_2[j])

for i in range(len(inces)):
    s=0
    for j in range(len(inces[i])):
        s+=1
        if i==inces[i][j]:
            s+=1
    print(f'У вершины {i+1} - {s//2} связей')
    if s == 0:
        zer=True #Это мы сразу ищем вершину с нулём для третьего задания
time.sleep(0.5)

#Задание 3
print("\n------------------------\n")
print("Ответ на третье задание:")
if zer:
    print('Существует вершина со степенью 0')
else:
    print('Не существует вершины со степенью 0')
time.sleep(0.5)

#Задание 4
print("\n------------------------\n")
print("Ответ на четвертое задание:")
print(f"{four} вершин инцидентно только одному ребру")
time.sleep(0.5)

#Задание 5
print("\n------------------------\n")
print("Ответ на пятое задание:")
five=[0 for i in range(n)]
for i in range(len(edge_1)):
    if edge_1[i]==edge_2[i]:
        five[edge_1[i]]+=1
for i in five:
    if i==max(five):
        print(f'Максимальное количество смежных между собой ребер, инцидентных одной и той же вершине - {i}')
        break
time.sleep(0.5)

#Задание 6
print("\n------------------------\n")
print("Ответ на шестое задание:")
for i in range(n):
    if graf[i][i]>=0:
        print('В графе есть петли')
        break

print("\n------------------------\n")
print('end.')