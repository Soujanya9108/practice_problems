a=input()
s=input()
e=0
d=999
for i in a:
    for j in s:
        c=abs(ord(i)-ord(j))
        print(c)
        if c<d:
            d=c
            e+=d    
print(e)
'''a=input()
s=input()
total=0
for i in a:
    if i not in s:
        temp=125
        for j in s:
            d=abs(ord(i)-ord(j))
            if d<temp:
                temp=d
    total+=temp 
print(total) '''             
   


