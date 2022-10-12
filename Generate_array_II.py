a=map(int,input().split())
s=list(map(int,input().split()))
l=[]
for i in range(0,len(s),2):
    l.append(str(s[i])*(s[i+1]))
    d=''.join(l)
print(*d)