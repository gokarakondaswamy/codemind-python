n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if (i%2!=0 and l[i]!=0) or (i%2==0 and l[i]%2!=0):
        c+=1
if c==n//2:
    print(True)
else:
    print(False)