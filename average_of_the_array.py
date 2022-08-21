n=int(input())
lst=list(map(int,input().split()))
s=(sum(lst)/n)
print("{:.2f}".format(s))