n=int(input())
lst=list(map(int,input().split()))
s=(sum(lst)//n)
if s in lst:
    print("True")
else:
    print("False")