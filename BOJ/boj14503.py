n, m = map(int, input().split())
r, c, d = map(int, input().split()) # 0: 북, 1: 동, 2: 남, 3: 서
arr = [list(map(int, input().split())) for _ in range(n)]

dir = [[-1,0],[0,1],[1,0],[0,-1]] # 북, 동, 남, 서
cnt = 0
clean = True

while clean : 
    if arr[r][c] == 0 : # 현재 칸이 청소되지 않은 경우
        arr[r][c] = 2 # 청소
        cnt += 1 # 청소하는 칸의 개수 증가
    
    flag = 0
    # 네 방향 확인하여 청소되지 않은 칸이 있는지 확인
    for _ in range(4) :
        d = (d+3)%4 # 반시계방향 : 북 > 서 > 남 > 동
        nr, nc = r + dir[d][0], c + dir[d][1] # 이동
        if 0 <= nr < n and 0 <= nc < m  and arr[nr][nc] == 0 : # 범위 내 있고 청소가 안됨
            r, c = nr, nc # 범위 내 없으면 for 문 반복
            break 
        flag += 1 # 이동할 수 없는 경우

    # 네 방향 모두 청소되어 있는 경우
    if flag == 4:
        nr, nc = r - dir[d][0], c - dir[d][1] # 후진 / 방향은 자동으로 원위치되어 있음
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] != 1: # 범위 내, 벽 아닌 경우 이동
            r, c = nr, nc
        else : # 후진 할 수 없는 경우
            clean = False
print(cnt)