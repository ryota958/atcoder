def main():
    N = int(input())
    ans = ""

    rem = N

    while rem:
        if rem % 2 == 1:
            ans += "A"
            rem -= 1
        else:
            ans += "B"
            rem //= 2

    print(ans[::-1])


if __name__ == '__main__':
    main()
