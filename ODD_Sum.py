n=int(input())
l=list(map(int,input().split()))
os=0
for i in range(0,n):
    if l[i]%2==0:
        continue
    else:
        os+=l[i]
        
print(os)