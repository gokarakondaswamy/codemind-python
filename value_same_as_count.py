n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    if l.count(i)==i:
        if i not in d:
            d.append(i)
print(len(d))