a,b=map(int,input().split())
l1=[]
l2=[]
l3=[]
for i in range(1,b+1):
    l1.append(a*i)
    l2.append(b*i)
for i in l1:
    if i in l2:
        l3.append(i)
print(min(l3))
