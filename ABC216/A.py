X, Y = map(int, input().split("."))
ans = str(X)
if 0 <= Y <= 2:
    ans += "-"
elif 3 <= Y <= 6:
    ans += ""          
else:
    ans += "+"
print(ans)
