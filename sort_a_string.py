n=input()
n1=sorted(n)
n2=[i for i in n1 if i.isalpha()]
#print(n2)
s=[0]*len(n)
#print(s)
for i in range(len(n)):
    if n[i].isalpha()!=True:
        s[i]=n[i]
#print(s)
i=0
j=0
while i<len(s):
    if s[i]==0:
        s[i]=n2[j]
        j+=1
    else:
        i+=1
print(''.join(s))