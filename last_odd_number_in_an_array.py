n=int(input())
s=list(map(int,input().split()))
l=[]
for i in range(len(s)):
    if s[i]%2!=0:
        l.append(s[i])
print(l[-1])