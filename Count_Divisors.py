a,b,x=map(int,input().split())
c=0
while (a<=b):
    if a%x==0:
        c+=1
    a+=1
print(c)