A, B = map(int, input().split())
for C in range(256):
    if (A==B or C==B) and not (A==B and C==B):
        print(C)
        break

