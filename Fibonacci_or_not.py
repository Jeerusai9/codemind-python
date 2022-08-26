n=int(input())
a=0
b=1
c=0
l=[]
l.append(a)
l.append(b)
for i in range(n):
    c=a+b
    l.append(c)
    a=b
    b=c
    c=0
if n in (l):
    print("True")
else:
    print("False")