n=int(input())
l=list(map(int,input().split()))
s=0
#print(l)
for i in l:
    if len(str(i))>s:
        s=len(str(i))
m=[i for i in l if len(str(i))==s]
print(*m)