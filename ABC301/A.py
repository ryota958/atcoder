N = int(input())
S = input()
x = 0
y = 0
for i in range(N):
    if S[i] == "T":
        x += 1
        if x == N/2