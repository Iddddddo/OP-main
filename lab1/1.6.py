a=int(input("Введите число: "))
a1=a//100
a2=(a//10)%10
a3=a%10
s=100*a3+10*a2+a1
print("Ответ: ", s)
