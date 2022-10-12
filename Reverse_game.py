def rev(n):
    a=0
    while n:
        r=n%10
        a=a*10+r
        n=n//10
    return a
n=int(input())
l=list(map(int,input().split()))
c=0
for i in (l):
    a=rev(i)
    print(a,end=' ')