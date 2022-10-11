n=int(input())
a=0
for i in range (n//2+1):
    if i*i==n:
        a=n
if a==n:
    print(True)
else:
    print('False')