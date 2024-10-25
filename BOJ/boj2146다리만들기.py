from collections import deque

n = int(input())
arr = [ list(map(int,input().split())) for _ in range(n)]
min_dis = 1e9
id = 2

# 섬 번호 표시
def makeid(r,c):
    global id
    arr[r][c] = id
    q = deque([(r,c)])
    while q :
        i, j = q.popleft()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]] :
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and  arr[ni][nj] == 1:
                arr[ni][nj] = id
                q.append((ni,nj))

for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 1 : # 섬이나, 섬번호를 부여받지 않은 경우
            makeid(i,j)
            id += 1 # 하나의 섬 종료, 섬번호 증가


# 다리 만들기
def bfs(cur_id): # cur_id : 현재 섬번호
    global min_dis
    visited = [[0]*n for _ in range(n)]# visited 배열 생성
    for i in range(n) : # 섬번호에 해당하는 곳 1처리
        for j in range(n) :
            if arr[i][j] == cur_id :
                visited[i][j] = 1

    q = deque([(i,j) for i in range(n) for j in range(n) if arr[i][j] == cur_id ])# 각 번호에 해당하는 섬을 큐에 넣고

    while q : # bfs 돌면서
        i, j = q.popleft()

        if visited[i][j] > min_dis : # visited(i,j까지 거리)가 min 값보다 크면 continue
            continue

        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]] :
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 :
                if arr[ni][nj] == 0 : # 섬이 없는 곳
                    q.append((ni,nj))
                    visited[ni][nj] = visited[i][j] + 1
                elif arr[ni][nj] != cur_id : # 만약 다른 섬을 만났다면
                    min_dis = min(min_dis, visited[i][j]) # min값 갱신

for i in range(2, id) :
    bfs(i)
print(min_dis-1)