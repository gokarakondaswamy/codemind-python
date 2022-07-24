a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
d=0
#print(b,c)
for i in l:
    if i<b or i>c:
        print(i, end=' ')
        d+=1
if d==0:
    print(-1)