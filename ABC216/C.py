def main():
    N = int(input())
    b = format(N, 'b')  # Nの2進数表記の文字列を得ます

    ans = ""

    for char in b:
        ans += "B"
        if char == "1":
            ans += "A"
    ans = ans[1:]  # 先頭に余計なBがあるので、取り除きます（しなくてもACできます）
    print(ans)


if __name__ == '__main__':
    main()
