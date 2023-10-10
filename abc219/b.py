s = [''] * 3
for i in range(3):
    s[i] = input()
t = input()
ans = ''
for i in range(len(t)):
    ans += s[int(t[i]) - 1]

print(ans)
