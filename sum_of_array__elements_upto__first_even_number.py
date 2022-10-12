n=int(input())
l=list(map(int,input().split()))
c=0
d=0
a=n//2
for i in range(n):
    c+=l[i]
    if l[i]%2==0:
        d=l[i]
        break
print(abs(c-d))