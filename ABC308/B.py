# 入力を受け取る
N, M = map(int, input().split())
color_price = dict()  # 色と価格の対応を保持する辞書
for _ in range(M):
    color, price = input().split()
    price = int(price)
    color_price[color] = price  # 辞書に追加
default_price = int(input())  # 一致しない色の料理の価格

total_price = 0  # 合計価格
for _ in range(N):
    color = input().strip()  # 皿の色
    total_price += color_price.get(color, default_price)  # 価格を合計に追加

print(total_price)  # 合計価格を出力
