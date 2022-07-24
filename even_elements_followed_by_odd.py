a=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if i%2==0:
        c+=[i]
for i in l:
    if i%2==1:
        c+=[i]
print(*c)