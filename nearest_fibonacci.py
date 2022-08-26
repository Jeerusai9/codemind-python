n=int(input())
l1=[]
l2=[]
l3=[]
a=0
b=1
l1.append(a)# a,b munde rayali endukate kavalsindi 1 tym 
l1.append(b)# for loop lo raste motham repeat avtundi
for i in range(n):
    c=a+b
    if c<n:
        l1.append(c)
    else:
        l2.append(c)
    a=b
    b=c
    c=0
x=abs(l1[-1]-n)# list 1 lo unde last element ni print chestunam
y=abs(l2[0]-n)# list 2 lo unde 1st element ni print chestunam
if x>y:# l1 lo unde last ele. l2 kanna > ayite l2 lo 1st element print
    print(l2[0])# n=10;-1 index no=8; 10-8=2;if 13-10=3
elif (y>x):# comparing to 2;3 2 chinnadi near ga undi so prnt 2
    print(l1[-1])#diff equal ayna a rendu no.s ni pint cheyali
elif (x==y):
    print(l1[-1],l2[0])