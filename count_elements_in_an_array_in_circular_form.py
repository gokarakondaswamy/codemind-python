n=int(input())
m=list(map(int,input().split()))
m.insert(0,m[-1])
m.append(m[1])
c=0
for i in range (0,n+2-1):
     if m[i+1]%2!=0 and m[i-1]%2==0 or m[i-1]%2!=0 and m[i+1]%2==0:
         c+=1
print(c)