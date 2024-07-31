a=input()
c=0
i=0
while i<=len(a)-1:
    if a[i]=="0" and a[i+1]=="0":
        c=c+1
        i=i+2
    else:
        c=c+1
        i=i+1
'''if i<len(a):
    c+=1        
print(c)'''