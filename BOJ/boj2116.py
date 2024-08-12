n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]  
idx = [5,3,4,1,2,0] 

def dice_(dice, i) : # i : 바닥면 인덱스
    global s
    if i == 0 or i == 5:
        s += max(dice[1:5])
    elif i == 1 or i == 3:
        s += max(dice[0], dice[2], dice[4], dice[5])
    elif i == 2 or i == 4:
        s += max(dice[0], dice[1], dice[3], dice[5])
    top = dice[idx[i]] # idx[i]는 윗면 인덱스, prev는 윗면 값
    return top


max_sum = 0
for start in range(6) :
    s = 0 # 주사위의 합
    top = dice_(dice[0], start) # start : 시작 바닥면, top: 대응하는 윗면
    for i in range(1, n) :
        bottom_idx = dice[i].index(top) # bottom_idx : 바닥면 인덱스
        top = dice_(dice[i], bottom_idx)
    if max_sum < s :
        max_sum = s
print(max_sum)