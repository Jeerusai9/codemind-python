n=int(input())
a=int(input()) #2 inputs tesukovali
l1=[]# 2 lists  teskovali
l2=[]
for i in range(1,n):# 50=range;50%i anedi ==0 ayite list loki pampi
    if n%i==0:
        l1.append(i)
for j in range(1,a):
    if a%j==0:
        l2.append(j)
if sum(l1)==a and sum(l2)==n:# l1 lo unde ele sum anedhi a equal and vice versa avvi ,print cheseyali
    print("Amicable")
else:
    print("Not Amicable")
