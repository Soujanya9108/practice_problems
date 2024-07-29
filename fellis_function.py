'''def fellis(n):
    if n==1 or n==0:
        return 1
    else:
        return fellis(n-1)+7*fellis(n-2)+(n//4)%(10**9+7)
print(fellis(8)) '''
x=[1,1]
n=int(input())
for i in range(2,n+1):
    ans=x[i-1]+7*x[i-2]+(i//4)%(10**9+7)
    x.append(ans)
print(x[n])
    