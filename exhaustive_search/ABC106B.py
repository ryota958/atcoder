N = int(input())
ans = 0
for n in range(1,N+1,2):
    sm = sum(n%i==0 for i in range(1,n+1))
    if sm==8:
        ans += 1
print (ans)