S = input()
S_set = set(S)
if len(S_set) == 1:
    print(1)
elif len(S_set) == 2:
    print(3)
else:
    print(6)
    