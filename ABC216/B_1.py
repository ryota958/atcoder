N = int(input())

S_set = set()

for _ in range(N):
    S = input()
    S_set.add(S)

print("Yes" if len(S_set) != N else "No")

