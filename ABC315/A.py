S = input()
S_new = S
for j in 'aiueo':
    S_new = S_new.replace(j, '')
print(S_new)