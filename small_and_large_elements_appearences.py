n=input().split()
c=''.join(n)
a=min(c)
b=max(c)
print(a,c.count(a),b,c.count(b),end=' ')