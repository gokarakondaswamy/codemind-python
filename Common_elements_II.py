a,b=map(int,input().split())
s=list(map(int,input().split()))
s1=list(map(int,input().split()))
l=[]
for i in s:
    if i not in s1 and i not in l:
            print(i,end=' ')
            l.append(i)
for i in s1:
    if i not in s and i not in l:
            print(i,end=' ')
            l.append(i)