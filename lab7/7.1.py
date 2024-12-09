import threading
import time
import random

abc='abcdefghijklmnopqrstuvwxyz'
sp=[]
c=0
s=''

def p1():
    global sp
    global abc
    global c
    global s
    while True:
        c+=1
        time.sleep(1.33)
        n=random.randint(20,30)
        for i in range(n):
            sp.append(abc[random.randint(0,len(abc)-1)])
        s=str(sp)[2:-2].replace("', '",'')

def p2():
    global s
    global c
    while True:
        c+=1
        time.sleep(2.1)
        print(s)

def p3():
    global sp
    global s
    global c
    global f
    while True:
        c+=1
        time.sleep(5)
        sp.sort()
        s=str(sp)[2:-2].replace("', '",'')
        f=open('lab7/text.txt','w')
        f.write(s)
        f.close()

t1 = threading.Thread(target=p1)
t2 = threading.Thread(target=p2)
t3 = threading.Thread(target=p3)
t1.start()
t2.start()
t3.start()
if c>= 100:
    t1.join()
    t2.join()
    t3.join()