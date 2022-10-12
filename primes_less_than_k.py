def prime(n):
    c=0
    for i in range(1,n//2+1):
        if n%i==0:
            c+=1
    if c==1:
        return True
n=int(input())
l=list(map(int,input().split()))
a=int(input())
c=[]
for i in (l):
    if i<=a:
        if prime(i)==True:c.append(i)
print(len(c))