M = int(input())
D = list(map(int, input().split()))
total = sum(D)
cnt = D[0]
for i in range(2, M):
    if cnt < int(total/2)+1:
        cnt += D[i]
    else:
        cnt += int((D[i]/2))
        break
print(cnt)