n=int(input())
sum1=0
b=str(n)
for i in range(len(b)):
    sum1=(sum1+int(b[i])**(i+1))
if sum1==n:
    print(True)
else:
    print(False)