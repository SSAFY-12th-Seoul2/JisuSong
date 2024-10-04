from itertools import combinations
from collections import deque

def diffuse(com):
    q = deque(com)

    while q :
        r, c = q.popleft()

        for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]] :
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] != 1 and arr2[nr][nc] == 0 and (nr, nc) not in com :
                arr2[nr][nc] = arr2[r][c] + 1
                q.append((nr,nc))

    min_time = 0
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 1 :
                continue
            elif (i,j) not in com and arr2[i][j] == 0 :
                return -1
            min_time = max(arr2[i][j], min_time)

    return min_time


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 2의 위치 파악
v = [(i,j) for i in range(n) for j in range(n) if arr[i][j] == 2]
ans = 1e9
for com in combinations(v,m) :
    arr2 = [[0]*n for _ in range(n)] # [[1 if arr[i][j] == 1 else 0 for j in range(n)] for i in range(n)]
    time = diffuse(com)
    if time != -1 :
        ans = min(ans, time)

if m == 0 :
    print(0)
elif ans == 1e9 :
    print(-1)
else :
    print(ans)