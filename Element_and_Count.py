n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if i not in c:
        a=l.count(i)
        print(i,a,end=' ')
        c.append(i)