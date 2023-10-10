N, K, A = map(int, input().split())
if (A + K) <= N:
    print()
else:
    print((A+K-1) % N)

