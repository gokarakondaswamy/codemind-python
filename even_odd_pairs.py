a=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2!=0:
        o.append(i)
    if i%2==0:
        e.append(i)
if len(e)>len(o):
    mi=len(o)
    y=e[mi:]
elif len(o)>len(e):
    mi=len(e)
    y=o[mi:]
else:
    mi=len(e)
for i in range(mi):
    print(e[i],o[i],end=' ')
for i in y:
    print(i,end=' ')
if len(y)%2==1:
    print(0)