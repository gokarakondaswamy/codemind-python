n=int(input())
a=0
for i in range(n//2+1):
    if i*(i+1) == n:
        a=n
if a==n:
    print('YES')
else:
    print('NO')