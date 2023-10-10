def main():
    X = input() #新しいアルファベット順
    D = dict() #辞書型
    #D[X[i]] = chr(ord('a') + i) #ord()は文字をASCIIコードに変換する関数
    for i in range(26):
        nxt = chr(ord('a') + i) 
        D[X[i]] = nxt 

    N = int(input())
    A = []
    for _ in range(N):
        S = input()
        T = ''
        for char in S:
            T += D[char]
        A.append((T, S)) 

    A.sort()

    for i in range(N):
        print(A[i][1])

if __name__ == '__main__':
    main()
