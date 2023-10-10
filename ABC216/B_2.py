#同姓同名の人がいるかどうかを判定する関数
def solve():
    for i in range(N):
        for j in range(N):
            if S[i] == S[j] and T[i] == T[j]:
                return True
    return False

N = int(input())

S = []
T = []
#名前と名字を別々にリストに格納する
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)
#solve()の返り値がTrueならばYesを、FalseならばNoを出力する
print("Yes" if solve() else "No")