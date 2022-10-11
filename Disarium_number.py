m=int(input())
n=m
s=0
def find(d):
    sd=str(d)
    return len(sd)
while m>0:
    s+=(m%10)**find(m)
    m=m//10
if s==n:
    print(True)
else:
    print(False)