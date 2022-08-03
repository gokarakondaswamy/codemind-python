n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(n):
    if i%2!=0 and l[i]%2!=0:
        c+=[i]
if len(c)==(n//2):
    print(True)
else:
    print(False)