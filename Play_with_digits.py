def ele(n):
    a=str(n)
    c=0
    for i in a:
        c+=int(i)
    return c
n=int(input())
l=list(map(int,input().split()))
c=0
for i in (l):
    a=ele(i)
    c+=a
print(c)
        