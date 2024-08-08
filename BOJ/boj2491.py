n = int(input())
lst = list(map(int, input().split()))

up = 1
down = 1
max_len = 1

for i in range(1, n) :
    if lst[i-1] >= lst[i] : # 같거나 높아지면 up+1
        up += 1
    else : # 낮아지면 1로 리셋
        up = 1

    if lst[i-1] <= lst[i] : # 같거나 낮아지면 down+1
        down += 1
    else : # 높아지면 1로 리셋
        down = 1

    if max_len < down: # 갱신
        max_len = down
    if max_len < up:
        max_len = up

print(max_len)