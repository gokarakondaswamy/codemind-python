n=int(input())
l=list(map(int,input().split()))
c=0
d=0
a=n//2
for i in (l):
    c+=i
    if i%2==1:
        d=i
        break
print(c-d)