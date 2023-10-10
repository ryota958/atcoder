A, B, C, X, Y = map(int, input().split())
ans = 10**10
for i in range(0, 2*max(X, Y)+1, 2):
    ans = min(ans, A*max(0, X-i//2)+B*max(0, Y-i//2)+C*i)
print(ans)