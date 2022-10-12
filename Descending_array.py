a=int(input())
s=list(map(int,input().split()))
b=sorted(s)
if s==sorted(s,reverse=True):
    print('yes')
else:
    print('no')