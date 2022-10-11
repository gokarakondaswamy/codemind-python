n=int(input())
l=list(map(int,input().split()))
i=0
a=len(l)-1
while i<a:
    print(l[i],l[a],end=' ')
    i+=1
    a-=1
if len(l)%2!=0:
    print(l[i],'0',end=' ')