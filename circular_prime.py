def prime(a):
    b=0
    for i in range(1,a//2+1):
        if a%i==0:
            b+=1
    if b==1:
        return True
    else:
        return False
def rev(a):
    s=0
    k=a
    while a>0:
        r=a%10
        s=s*10+r
        a=a//10
    return s
n=int(input())
m= rev(n)
if prime(n)==True and prime(m)==True:
    print('circular prime')
elif prime(n)==True:
    print('prime but not a circular prime')
else:
    print('not prime')