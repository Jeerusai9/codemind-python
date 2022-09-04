n=int(input())
a=str(n)
b=n**2
c=int(a[::-1])
d=str(c**2)
e=d[::-1]
if b==int(e):
    print("True")
else:
    print("False")