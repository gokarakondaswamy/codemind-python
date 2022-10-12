def div (n,k):
    if n%k==0:
        return True
n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in (l):
    if div(i,k)==True:
        c+=1
print(c)