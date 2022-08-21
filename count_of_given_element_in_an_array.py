n=int(input())
s=list(map(int,input().split()))
a=int(input())
c=0
if a in s:
    for i in s:
        if i==a:
            c=c+1
    print(c)
else:
    print(0)