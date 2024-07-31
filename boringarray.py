'''n=int(input())
a=list(map(int,input().split()))
a.sort()
print(a)
j=n-1
b=[]
ans=0
for i in range(0,n):
    if i<=j:
         c=abs(a[i]-a[j])
         b.append(c)
         j-=1
for i in b:
    ans=ans+i
print(ans)'''


n=int(input())
a=list(map(int,input().split()))
a.sort()
print(a)
i=0
j=len(a)-1
s=0
while i<=j:
    c=abs(a[i]-a[j])
    s+=c
    j-=1
    i+=1
print(s)



