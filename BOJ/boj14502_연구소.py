from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [(i, j) for i in range(N) for j in range(M) if arr[i][j] == 2] # 바이러스 위치
wall = len([(i, j) for i in range(N) for j in range(M) if arr[i][j] == 1]) # 벽의 개수
max_safe = 0 # 최대 안전구역

# 세 곳에 벽 세우기
def dfs(c):
    global max_safe
    if c == 3 :
        max_safe = max(max_safe,bfs(arr))
        return

    for i in range(N):
        for j in range(M) :
            if arr[i][j] == 0 : # 벽을 세울 수 있는 곳
                arr[i][j] = 1
                dfs(c+1)
                arr[i][j] = 0

# bfs로 바이러스 확산 후, 안전구역 확인
def bfs(arr) :
    global v
    q = deque(v) # 2(바이러스)가 있는 위치에서 시작
    visited = [[0]*M for _ in range(N)]
    virus_num = 0 # 바이러스 확산 칸 수
    while q :
        r, c = q.popleft()
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)] :
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited[nr][nc] == 0 :
                virus_num += 1
                visited[nr][nc] = 1
                q.append((nr,nc))

    # print(N*M, wall, virus_num, len(v))
    return N*M - wall - virus_num - len(v) - 3

dfs(0)
print(max_safe)