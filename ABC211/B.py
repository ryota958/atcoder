S = [0] * 4
S[0] = input()
S[1] = input()
S[2] = input()
S[3] = input()

if S.count("H") == 1 and S.count("2B") == 1 and S.count("3B") == 1 and S.count("HR") == 1:
    print("Yes")
else:
    print("No")
