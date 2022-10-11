def prime(n):
    if n==1:
        return False
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=1
    if c==1:
        return True
    else:
        return False
n=int(input())
#m=int(input())
c=[]
for i in range (1,n):
    if n%i==0:
        if prime(i)==False:c.append(i)
print(len(c)+1)