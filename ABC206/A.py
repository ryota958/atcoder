import math

N = int(input())
x = 1.08 * N
result = math.floor(x)
if result < 206:
    print("Yay!")
elif result == 206:
    print("so-so")
else:
    print(":(")
