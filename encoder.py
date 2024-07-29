n=167
def sod(n):
    c=0
    while n>0:
        c=c+1
        n=n//10
    return c
def rev(n):
    ans=0
    while n>0:
        digit=n%10
        sq=digit**2
        sod_sq=sod(sq)
        ans=ans*(10**sod_sq)+sq
        n=n//10
    return ans
ans=rev(n)
def rev2(n):
    a1=0
    while n>0:
        d=n%10
        a1=a1*10+d
        n=n//10
    return a1
print(rev2(ans))            