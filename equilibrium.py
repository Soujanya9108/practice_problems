a=[2,1,1,2,4,2]
f=0
for i in range(0,len(a)):
    i1=i
    j=i+1
    s=0
    s1=0
    while(i>=0):
        s=s+a[i]
        i=i-1
    while(j<len(a)):
        s1=s1+a[j]
        j=j+1
    if(s==s1):
        print(i1)
        f=1
        break
if f==0:
    print(len(a)//2)
