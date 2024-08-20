def diffusion() :
    for i in range(r) :
        for j in range(c) :
            if arr[i][j] > 0 :
                v = arr[i][j]//5 # 확산되는 양
                cnt = 0  # 확산된 방향 개수
                # (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산
                for dr, dc in dir :
                    nr, nc = i + dr, j + dc
                    # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
                    if 0<= nr < r and 0<= nc < c and arr[nr][nc] != -1 :
                        new[nr][nc] += v
                        cnt += 1
                new[i][j] += arr[i][j] - v*cnt

def working(arr):
    # 공기청정기 위쪽
    for i in range(cleaning[0]-1,0,-1) :
        arr[i][0] = arr[i-1][0]
    arr[0][:c - 1] = arr[0][1:]
    for i in range(cleaning[0]) :
        arr[i][c-1] = arr[i+1][c-1]
    arr[cleaning[0]][1:] = [0] + arr[cleaning[0]][1:c - 1]

    for i in range(cleaning[1]+1,r-1) :
        arr[i][0] = arr[i+1][0]
    arr[-1][:c - 1] = arr[-1][1:]
    for i in range(r-1, cleaning[1],-1) :
        arr[i][c-1] = arr[i-1][c-1]
    arr[cleaning[1]][1:] = [0] + arr[cleaning[1]][1:c - 1]

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
dir = [[1,0],[-1,0],[0,1],[0,-1]]
# 공청기 위치 찾기
for i in range(r) :
    if arr[i][0] == -1 :
        cleaning = [i,i+1]
        break

for _ in range(t) : # t초 동안
    new = [[0] * c for _ in range(r)]  # 미세먼지 확산 정보를 담을 리스트
    new[cleaning[0]][0] = -1
    new[cleaning[1]][0] = -1
    # (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산
    diffusion()
    # 공기청정기가 작동
    working(new)
    arr = new

print(sum([sum(row) for row in arr])+2)