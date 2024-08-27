########### 제출 1 ############
# 모든 부분 격자를 시계 방향으로 90도 회전
def spin(L, origin) :
    tmp_arr = [[0] * 2**n for _ in range(2**n)]  #  새로운 배열
    for i in range(0,2**n,2**L): # 격자를 2L × 2L 크기의 부분 격자로 나눈다.
        for j in range(0,2**n,2**L):
            x1,y1,x2,y2 = i,j,i+2**L-1,j+2**L-1 # 왼쪽 상단, 오른쪽 하단
            new = list(zip(*origin[x1:x2+1][::-1]))[y1:y2+1] # 해당 부분 잘라서 시계방향으로 돌림
            idx = 0
            for x in range(x1,x2+1) :
                tmp_arr[x][y1:y2+1] = new[idx]
                idx += 1
    return tmp_arr

def melt(arr):
    tmp_arr = [[0] * 2 ** n for _ in range(2 ** n)]  # 새로운 배열, 그냥 arr 쓰면X
    for i in range(2**n):
        for j in range(2**n):
            cnt = 0
            for di, dj in [[0,1],[0,-1],[1,0],[-1,0]] :
                ni, nj = i + di, j + dj
                if 0 <= ni < 2**n and 0 <= nj < 2**n and arr[ni][nj] > 0 :
                    cnt += 1
            if cnt < 3 : # 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸
                tmp_arr[i][j] = max(arr[i][j] - 1,0) # 얼음의 양이 1 줄어든다
            else :
                tmp_arr[i][j] = arr[i][j]
    return tmp_arr

# 남아있는 얼음 A[r][c]의 합
def sum_total(arr) :
    s = 0 # 남아있는 얼음 A[r][c]의 합
    max_c = 0 # 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
    visited = [[0] * 2 ** n for _ in range(2 ** n)]

    for i in range(2**n):
        for j in range(2**n):
            if visited[i][j] == 0 :
                visited[i][j] = 1
                c = 0
                if arr[i][j] > 0 :
                    c = 1 # 칸의 개수
                    s += arr[i][j] # 얼음 수
                    q = [(i, j)]
                    while q :
                        ci, cj = q.pop(0)
                        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                            ni, nj = ci + di, cj + dj
                            if 0 <= ni < 2 ** n and 0 <= nj < 2 ** n and arr[ni][nj] > 0 and visited[ni][nj] == 0:
                                c += 1
                                s += arr[ni][nj]
                                visited[ni][nj] = 1
                                q.append((ni,nj))

            if max_c < c :
                max_c = c
    return s, max_c

## 입력
n, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**n)]
L = list(map(int,input().split()))
for i in range(q) :
    arr = spin(L[i], arr) # 회전
    arr = melt(arr) # 얼음양 감소
s, max_c = sum_total(arr)
print(s)
print(max_c)


########### 제출 2 ############
# 모든 부분 격자를 시계 방향으로 90도 회전
def spin(L, origin) :
    tmp_arr = [[0] * 2**n for _ in range(2**n)]  #  새로운 배열
    for i in range(0,2**n,2**L): # 격자를 2L × 2L 크기의 부분 격자로 나눈다.
        for j in range(0,2**n,2**L):
            x1,y1,x2,y2 = i,j,i+2**L-1,j+2**L-1 # 왼쪽 상단, 오른쪽 하단
            new = list(zip(*origin[x1:x2+1][::-1]))[y1:y2+1] # 해당 부분 잘라서 시계방향으로 돌림
            idx = 0
            for x in range(x1,x2+1) :
                tmp_arr[x][y1:y2+1] = new[idx]
                idx += 1
    return tmp_arr

def melt(arr):
    tmp_arr = []
    for i in range(2**n):
        for j in range(2**n):
            if arr[i][j] > 0 :
                cnt = 0
                for di, dj in [[0,1],[0,-1],[1,0],[-1,0]] :
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 2**n and 0 <= nj < 2**n and arr[ni][nj] > 0 :
                        cnt += 1
                if cnt < 3 : # 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸
                    tmp_arr += [(i,j)]
    for i, j in tmp_arr :
        arr[i][j] -= 1
    return arr

# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
def sum_total(arr) :
    max_c = 0 # 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
    visited = [[0] * 2 ** n for _ in range(2 ** n)]

    for i in range(2**n):
        for j in range(2**n):
            if visited[i][j] == 0 and arr[i][j] > 0 :
                visited[i][j] = 1
                c = 1 # 칸의 개수
                q = [(i, j)]
                while q :
                    ci, cj = q.pop(0)
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < 2 ** n and 0 <= nj < 2 ** n and arr[ni][nj] > 0 and visited[ni][nj] == 0:
                            c += 1
                            visited[ni][nj] = 1
                            q.append((ni,nj))

                max_c = max(max_c, c)
    return max_c

## 입력
n, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**n)]
L = list(map(int,input().split()))
for i in range(q) :
    arr = spin(L[i], arr) # 회전
    arr = melt(arr) # 얼음양 감소
print(sum([sum(row) for row in arr]))
print(sum_total(arr))



########### 제출 3 ############
# 모든 부분 격자를 시계 방향으로 90도 회전
def spin(L, origin):
    tmp_arr = [[0] * (2**n) for _ in range(2**n)]
    step = 2**L
    for i in range(0, 2**n, step):
        for j in range(0, 2**n, step):
            for x in range(step):
                for y in range(step):
                    tmp_arr[i + y][j + step - 1 - x] = origin[i + x][j + y]
    return tmp_arr

def melt(arr):
    tmp_arr = [[0] * 2 ** n for _ in range(2 ** n)]  # 새로운 배열, 그냥 arr 쓰면X
    for i in range(2**n):
        for j in range(2**n):
            cnt = 0
            for di, dj in [[0,1],[0,-1],[1,0],[-1,0]] :
                ni, nj = i + di, j + dj
                if 0 <= ni < 2**n and 0 <= nj < 2**n and arr[ni][nj] > 0 :
                    cnt += 1
            if cnt < 3 : # 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸
                tmp_arr[i][j] = max(arr[i][j] - 1,0) # 얼음의 양이 1 줄어든다
            else :
                tmp_arr[i][j] = arr[i][j]
    return tmp_arr

# 남아있는 얼음 A[r][c]의 합
def sum_total(arr) :
    s = 0 # 남아있는 얼음 A[r][c]의 합
    max_c = 0 # 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
    visited = [[0] * 2 ** n for _ in range(2 ** n)]

    for i in range(2**n):
        for j in range(2**n):
            if visited[i][j] == 0 :
                visited[i][j] = 1
                c = 0
                if arr[i][j] > 0 :
                    c = 1 # 칸의 개수
                    s += arr[i][j] # 얼음 수
                    q = [(i, j)]
                    while q :
                        ci, cj = q.pop(0)
                        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                            ni, nj = ci + di, cj + dj
                            if 0 <= ni < 2 ** n and 0 <= nj < 2 ** n and arr[ni][nj] > 0 and visited[ni][nj] == 0:
                                c += 1
                                s += arr[ni][nj]
                                visited[ni][nj] = 1
                                q.append((ni,nj))

            if max_c < c :
                max_c = c
    return s, max_c

## 입력
n, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**n)]
L = list(map(int,input().split()))
for i in range(q) :
    arr = spin(L[i], arr) # 회전
    arr = melt(arr) # 얼음양 감소
s, max_c = sum_total(arr)
print(s)
print(max_c)