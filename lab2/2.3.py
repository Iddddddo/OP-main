s=input('input: ')
s=s.split(',')
summ=0
print('a:',s[3])
print('b:',end=' ')
for i in range(len(s)):
    print(s[-i], end=' ')
    summ+=int(s[i])
print('')
print('c:',summ, summ/6)