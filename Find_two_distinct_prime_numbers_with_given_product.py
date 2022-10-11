def prime(n):
    c=0
    for i in range (1,n//2+1):
        if n%i==0:
            c+=1
    if c==1:
        return True
    else:
        return False
n=int(input())
c=[]
b=[]
for i in range(1,n//2+1):
    if n%i==0:
        c.append(i)
for i in c:
    if prime(i)==True:
        b.append(i)
if len(b)>1:
    print(*b)
else:
    print(-1)
            