N = int(input())
for i in range(1, 10):# 1~9
    for j in range(1, 10):# 1~9
        if i * j == N:
            print("Yes")
            exit()
print("No")