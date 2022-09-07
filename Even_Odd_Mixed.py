n=int(input())
c=str(n)
eo=0
oc=0
for i  in range(len(c)):
    if int(c[i])%2==0:
        eo+=1
for j in range(len(c)):
    if int(c[j])%2==1:
        oc+=1
if eo==len(c):
    print("Even")
elif oc==len(c):
    print("Odd")
else:
    print("Mixed")