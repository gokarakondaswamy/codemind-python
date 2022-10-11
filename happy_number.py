n=int(input())
y=n
def sq(n):
    s=0
    while n:
        r=n%10
        s=s+(r*r)
        n=n//10
    return s
while y!=1 and y!=4:
    y=sq(y)
if y==1:
    print(True)
else:
    print(False)
        