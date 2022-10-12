def rev(n):
    j=n
    a=0
    while n:
        r=n%10
        a=a*10+r
        n=n//10
    if a==j:
        return True
n=int(input())
l=list(map(int,input().split()))
c=0
for i in (l):
    if rev(i)==True:
        c+=1
print(c)