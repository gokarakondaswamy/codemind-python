n=int(input())
l=list(map(int,input().split()))
c=[]
a=0
for i in l:
    if l.count(i)==i:
        if i not in c:
            a+=i
            c.append(i)
if len(c)>=1:
    print('{:.2f}'.format(a/len(c)))
else:
    print(-1)