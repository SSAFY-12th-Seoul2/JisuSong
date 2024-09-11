from itertools import combinations
import copy
# D 이하인 적 중에서 가장 가까운 적
def find_e(c) :
    min_dis = n + m
    near_enemy = None
    for i, j in enemy :
        dis = abs(n-i) + abs(c-j)
        if dis <= d : # D 이하인 적 중
            if dis < min_dis : # 가장 가까운 적
                min_dis = dis
                near_enemy = (i,j)
            elif dis == min_dis and j < near_enemy[1] : # 가장 왼쪽에 있는 적
                near_enemy = (i,j)
    if near_enemy is not None :
        enemy_info.add(near_enemy)


n, m, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
enemy_ = [(i,j) for i in range(n) for j in range(m) if arr[i][j] == 1] # 처음 적 위치 파악
max_attack = 0

tmp = list(range(m))
for col in combinations(tmp,3) : # 궁수 자리 확정
    enemy = copy.deepcopy(enemy_)
    attack = 0 # 이번 궁수들의 공격 횟수

    while enemy :# 모든 적이 격자판에서 제외되면 게임이 끝난다.
        enemy_info = set() # 가장 가까운 적을 받아옴
        for c in col :
            find_e(c)

        # 적이 가장 가까운 적이었다면 공격받고, 아니면 이동
        for _ in range(len(enemy)):
            i,j = enemy.pop(0)
            if (i,j) in enemy_info : # 공격받은 적은 게임에서 제외
                attack += 1
            else : # 적이 이동
                if i+1 < n : # 적은 아래로 한 칸 이동, 성이 있는 칸으로 이동한 경우에는 게임에서 제외
                    enemy.append((i+1,j))

    max_attack = max(max_attack, attack)
print(max_attack)
