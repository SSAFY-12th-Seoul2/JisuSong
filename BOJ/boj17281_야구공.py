from itertools import permutations

N = int(input())
scores = [list(map(int, input().split())) for _ in range(N)]
max_s = 0 # 최대 득점


# 1번 선수를 제외한 순열생성
o = [1,2,3,4,5,6,7,8]
orders = permutations(o,8)

for order in orders :
    order = list(order)
    order.insert(3,0)
    s = 0 # 득점수
    batter = 0 # 타자
    inning = 0
    out = 0
    ru = [0, 0, 0]  # 1,2,3루
    while inning < N :
        result = scores[inning][order[batter]]
        if result == 0: # 아웃
            out += 1
            if out == 3 :
                inning += 1
                out = 0
                ru = [0,0,0]
        elif result == 1: # 안타
            s += ru[2]
            ru[2] = 0
            if ru[1] == 1 :
                ru[2] = 1
                ru[1] = 0
            if ru[0] == 1:
                ru[1] = 1
            ru[0] = 1
        elif result == 2: # 2루타
            s += ru[1] + ru[2]
            ru[2], ru[1] = 0, 0
            if ru[0] == 1:
                ru[2] = 1
                ru[0] = 0
            ru[1] = 1
        elif result == 3: # 3루타
            s += ru[0] + ru[1] + ru[2]
            ru = [0,0,1]
        elif result == 4: # 홈런
            s += ru[0] + ru[1] + ru[2] + 1
            ru = [0, 0, 0]

        batter = (batter + 1) % 9 # 다음 타자

    max_s = max(max_s, s)

print(max_s)