import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
total_sec = 0 # 초

# 아기상어 위치 파악
for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 9 :
            shark_r, shark_c = i, j
            arr[i][j] = 0
            break
size = 2

def move() :
    global shark_r, shark_c, total_sec, size
    visited = [[0]*n for _ in range(n)] # 이동 거리 저장용
    visited[shark_r][shark_c] = 1
    fish = [[0]*n for _ in range(n)] # 먹을 수 있는 물고기 거리 저장용
    min_dis = 1e9 # 최소 거리
    q = deque([(shark_r, shark_c)])
    while q :
        r, c = q.popleft()
        for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]] : # 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동
            nr, nc = r +dr , c + dc
            # 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] <= size and visited[nr][nc] == 0 :
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr,nc))
                if 0 < arr[nr][nc] < size : # 자신의 크기보다 작은 물고기만 먹을 수 있다.
                    fish[nr][nc] = visited[nr][nc] # 먹을 수 있는 물고기 거리 저장
                    if min_dis > visited[nr][nc] : # 최소 거리 업데이트
                        min_dis = visited[nr][nc]

    for i in range(n):
        for j in range(n) :
            if fish[i][j] == min_dis :
                arr[i][j] = 0  # 물고기를 먹으면, 그 칸은 빈 칸이 된다.
                shark_r, shark_c = i, j # 이동
                total_sec += min_dis-1 # 물고기 먹는데 걸린 시간
                return 1
    return 0

eat = 0
while True :
    # 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
    if move() : # 먹은 물고기 존재
        eat += 1
        if eat == size :
            eat = 0
            size += 1
    else : # 먹을 수 있는 물고기 없음
        print(total_sec)
        break