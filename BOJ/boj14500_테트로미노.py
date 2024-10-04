n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max_val = 0

def dfs(i,j,c) :
    global max_val, s
    if c == 4 :
        max_val = max(max_val,s)
        return

    for di, dj in [[0,1],[0,-1],[1,0],[0,-1]] :
        ni, nj = i + di, j + dj
        if 0<=ni<n and 0<=nj<m and visited[ni][nj] == 0 :
            visited[ni][nj] = 1
            s += arr[ni][nj]
            dfs(ni,nj,c+1)
            visited[ni][nj] = 0
            s -= arr[ni][nj]

def dfs2(i,j): # ㅗ ㅜ ㅓ ㅏ
    global max_val
    tmp = []
    for di, dj in [[0,1],[0,-1],[1,0],[-1,0]] :
        ni, nj = i+di, j+dj
        if 0<=ni<n and 0<=nj<m:
            tmp += [(ni,nj)]
    if len(tmp) >= 3 :
        for k in range(len(tmp)) :
            s = arr[i][j] + arr[tmp[k][0]][tmp[k][1]] + arr[tmp[(k+1)%len(tmp)][0]][tmp[(k+1)%len(tmp)][1]] + arr[tmp[(k+2)%len(tmp)][0]][tmp[(k+2)%len(tmp)][1]]
            max_val = max(max_val, s)

visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        s = arr[i][j] # 네 칸의 합을 담을 변수
        dfs(i,j,1)
        visited[i][j] = 0
        dfs2(i,j)
print(max_val)
