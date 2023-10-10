N = int(input())

p = list(map(int, input().split()))
q = [0] * N

for i in range(N):
    p_i = p[i] - 1
    q[p_i] = i + 1

print(*q)
