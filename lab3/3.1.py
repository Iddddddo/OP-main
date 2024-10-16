s=input()
if s[-1] == '.':
    s=s[:-1]
    s+=' '
print(len(s))
print(len(s.split()))
a=s.split()
for i in range(len(a)):
    a[i]=len(a[i])
print(str(min(a)), str(max(a)))
