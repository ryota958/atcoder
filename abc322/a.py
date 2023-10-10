def find_abc_position(s, n):
    # 文字列sを走査
    for i in range(n-2):
        # i番目からi+2番目までの部分文字列が'ABC'であるかをチェック
        if s[i:i+3] == 'ABC':
            # 'ABC'が見つかった場合、i+1を返す（1-indexed）
            return i + 1
    # 'ABC'が見つからなかった場合、-1を返す
    return -1

# 例: 文字列sが'ABABC'の場合
n = int(input())
s = input()

result = find_abc_position(s, n)
print(result)  # Output: 3

