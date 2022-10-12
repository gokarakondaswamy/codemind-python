n=input().split()
s=0
e=0
for i in n:
    s+=ord(min(i))
    e+=ord(max(i))
print(abs(s-e))
    