def check_string(s):
    # | の位置を取得
    pos1 = s.find("|")
    pos2 = s.find("|", pos1 + 1)
    
    # * の位置を取得
    pos_star = s.find("*")
    
    # 条件を判定
    if pos1 < pos_star and pos2 > pos_star:
        return "in"
    else:
        return "out"

N = int(input())
S = map(str, input().split())
 check_string(S)