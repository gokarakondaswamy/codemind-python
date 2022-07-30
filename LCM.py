a,b=map(int,input().split())
c=[]
d=[]
for i in range(a,a**3,a):
    c+=[i]
for j in range(b,b**3,b):
    d+=[j]
e=set(d).intersection(set(c))
print(min(e))
