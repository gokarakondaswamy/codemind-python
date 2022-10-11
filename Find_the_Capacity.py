a,b,c=map(int,input().split())
c=2*a*b*c*512
d=str(c//1024)
print(d+'KB')