s=input()
if s[-1] == '.':
    s=s[:-1]
    s+=' '
print(len(s))
print(len(s.split()))
print(len(str(min(s.split()))), len(str(max(s.split()))))
