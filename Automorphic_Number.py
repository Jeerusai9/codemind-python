n=int(input())
s=str(n)# 5 tesukunte string lo convert chesukovali'5' ni
s1=n**2# danini sqre cheyali 5^2=25)
s2=str(s1)# vachina 25 ni strings lo convert chesukovali='2','5'
s3=s2[-len(s):] #accessing of elements =n; i.e = n=5 unte string lo unde 5 elements
if n==int(s3):##if n aneddhi s3 string length (int) equal ayite automorphic
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")