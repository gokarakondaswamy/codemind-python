n=int(input())
l=list(map(int,input().split()))
c=0
d=0
a=n//2
for i in range(n):
    if i<a:
        c+=l[i]
    if i>=a:
        d+=l[i]
print(abs(c-d))
