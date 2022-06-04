n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in range(a,b+1):
    c+=[i]
s=set(l)
g=set(c)
f=s.difference(g)
print(sum(f))
    