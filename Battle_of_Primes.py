def prime(a):
    b=0
    for i in range(1,a//2+1):
        if a%i==0:
            b+=1
    if b==1:
        return True
    else:
        return False
def nprime(a):
    while prime(a)==False:
        a=a+1
    return a
n=int(input())
m=int(input())
u=m+n
p=nprime(u)
if prime (u)==True:
    p=nprime(u+1)
    print(p-u)
else:
    print(p-u)