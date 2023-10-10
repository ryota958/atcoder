def check_conditions(s):
    # 全ての条件を確認する
    if all(100 <= x <= 675 and x % 25 == 0 for x in s) and all(s[i] <= s[i+1] for i in range(len(s)-1)):
        return "Yes"
    else:
        return "No"

s = list(map(int, input().split()))  # 整数を入力する
print(check_conditions(s))  # 条件を確認し、結果を出力する

