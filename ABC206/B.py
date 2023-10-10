n = int(input())

i = 1
money = 0

while True:
    money += i
    if money >= n:
        break
    i += 1

print(i)