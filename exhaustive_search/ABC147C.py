N = int(input())

evidnece = [[] for _ in range(N)]
for i in range(N):
    A = int(input())
    for _ in range(A):
        x, y = map(int, input().split())
        evidnece[i].append((x-1, y))

ans = 0
for i in range(1, 2**N):
    consistent = True
    for j in range(N):
        if (i >> j) & 1:
            for x, y in evidnece[j]:
                if ((i >> x) & 1) != y:
                    consistent = False
                    break
            if not consistent:
                break
    if consistent:
        ans = max(ans, bin(i).count('1'))

print(ans)