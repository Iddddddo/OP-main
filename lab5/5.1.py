with open("lab5/in.txt", "r", encoding="utf-8") as f:
    text = f.read()
a=text.split()
s=''
k=0
for i in a:
    s+= f'{i} '
    k+=1
    if k==7:
        s+='\n'
        k=0
with open('out.txt', 'w', encoding="utf-8") as file:
    file.write(s)