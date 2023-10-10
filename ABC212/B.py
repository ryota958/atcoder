X = input()
if X[0] == X[1] == X[2] == X[3]:
    print("Weak")
    exit()
for i in range(3):
    if (int(X[i])+1)%10 != int(X[i+1]):
        print("Strong")
        exit()
print("Weak")

