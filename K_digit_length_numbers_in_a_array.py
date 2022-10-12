n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
#print(l)
for i in l:
    b=abs(i)
    a=str(b)
    if len(a)==k:
        c+=1
print(c)