n=int(input())
l=list(map(int,input().split()))
a=int(input())
c=0
for i in l:
    c+=i
    if i==a:
        break
print(c)