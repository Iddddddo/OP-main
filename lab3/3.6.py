import random
T=[[[random.randint(1,100) for j in range(7)] for i in range(5)]for l in range(3)]

a=[]
for i in T:
    for j in i:
        for k in j:
            a.append(k)
big_x=max(a)
I=0
for i in range(len(a)):
    if a[i]==big_x:
        I=i
        break
x, y, z=I//35+1, (I%35)//7+1, ((I%35)%7)+1

for j in T:
    print(j)

print(f'x:{y}, y:{4-x}, z:{z}, eq={big_x}')
'''Ответ в формате xyz системы координат, x-номер блока в горизонтали, y-номер строки, z-номер элемента в блоке x'''