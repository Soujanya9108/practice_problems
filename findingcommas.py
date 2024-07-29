n=int(input())
c=1000
ans=0
k=1
while c<=n:
    m=c*1000
    num=min(n-c+1,m-c)
    ans+=num*k
    c=m
    k=k+1
print(ans)    