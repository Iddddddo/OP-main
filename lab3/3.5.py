'''
Ввести с помощью генератора случайных чисел целочисленную матрицу размерности
n×m (заданы константами). Найти максимальный элемент среди элементов с нечетной
суммой индексов. Вывести на экран найденный элемент, его индексы.
'''
import random

n,m=map(int, input().split())
matr = [[random.randint(0,100) for i in range(n)] for j in range(m)]
for i in range(n):
    for j in range(m):
        if (i+j) % 2 == 0:
            matr[j][i]=0

gor=0
ver=0
big=0

for i in range(m):
    if max(matr[i])>big:
        big=max(matr[i])
        ver=i
for i in range(n):
    if matr[ver][i]==big:
        gor=i

print('---')
for i in range(n):
    for j in range(m):
        print('{:>2d}'.format(matr[j][i]), end=' ')
    print()
print('---')

print(f'Строка: {gor+1}, столбец: {ver+1}, Значение: {big}')