n=int(input())# 5124 tesukunte
s=str(n)# '5','1','2','4' string lo convert chesam
l=0#count=0
for i in s:
    if s.count(i)==1:#5 vastundi adi 1 sari undi so next malli inlodaniki place ivvali
        l+=1
if l==len(s):# ala vachina count==length ki equal ayite unique
    print("Unique Number")
else:
    print("Not Unique Number")