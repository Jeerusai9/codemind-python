n=int(input())
lst=list(map(int,input().split()))
s=int(input())
for i in range(s):
    if s in lst:
        print("True")
        break
else:
    
    print("False")