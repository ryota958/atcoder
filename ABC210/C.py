N, K = map(int, input().split())
C = list(map(int, input().split()))
ans = 0
for i in range(N-K+1):
    if len(set(C[i:i+K])) > ans:
        ans = len(set(C[i:i+K]))
print(ans)
