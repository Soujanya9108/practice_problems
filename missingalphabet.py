n="abcdefghijklmnopqrstuvwxyz"
s=input()
ans=""
for i in n:
    if i not in s:
        ans=ans+i
print(ans)        