s=input("Введите число: ")
a=int(s)
a1=a//100
a2=(a//10)%10
a3=a%10
print(a1,a2,a3)
print('Сумма: ',a1+a2+a3,'Произведение: ',a1*a2*a3)