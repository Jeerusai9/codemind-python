n=int(input())
l=list(map(int,input().split()))
es=0
for i in range(0,n):
    if l[i]%2==0:
        es+=l[i]
    else:
        continue
print(es)