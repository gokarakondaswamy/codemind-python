def check(a,n):
    ma=a[1]-a[0]
    for i in range(1,n-1):
        if ((a[i]>a[i-1] and a[i+1]<a[i])or (a[i]<a[i-1]and a[i+1]>a[i])):
            ma=max(ma,abs(a[i]-a[i+1]))
        else:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
wave=(n-1)//2
if check(l,n):
    print('yes')
else:
    print('no')