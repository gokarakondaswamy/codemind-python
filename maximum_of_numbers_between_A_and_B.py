n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in l:
    if i>=a and i<=b:
        c.append(i)
if len(c)>=1:
    print(max(c))
else:
    print(-1)
        