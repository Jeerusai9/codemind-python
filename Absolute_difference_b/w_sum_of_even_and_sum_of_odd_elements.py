n=int(input())
l=list(map(int,input().split()))
s=0
d=0
for i in range(0,len(l)):
    if l[i]%2==0:
        s+=l[i]
    else:
        d+=l[i]
c=abs(s-d)
print(c)