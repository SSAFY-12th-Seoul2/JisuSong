from itertools import combinations
import sys
input = sys.stdin.readline

def down(arr, start) :
    r, c = 0, start
    visited = [[0] * n for _ in range(h)]
    while r < h : # 마지막 행까지
        # print(r,c)
        if arr[r][c] > 0 : #사다리가 있는 경우
            visited[r][c] = 1
            if 0 < c and arr[r][c-1] == arr[r][c] and visited[r][c-1] == 0:
                visited[r][c-1] = 1
                c -= 1
            elif c < n-1 and arr[r][c+1] == arr[r][c] and visited[r][c+1] == 0 :
                visited[r][c+1] = 1
                c += 1
            else :
                r += 1
        else :
            r += 1
    return c

def check(arr):
    global min_ladder
    for i in range(n):
        # print( i,'번째 세로선 시작')
        if i != down(arr, i): # 처음 시작 칼럼이랑 도착 칼럼이랑 다른 경우
            return 0
    return 1

# 입력
n, m, h = map(int, input().split())
arr = [[0]*n for _ in range(h)]

# 다리놓기
tmp = 1 # 다리 번호
for _ in range(m) :
    a, b = map(int, input().split())
    arr[a-1][b-1] = tmp
    arr[a-1][b] = tmp
    tmp += 1

# 사다리 후보 만들기
ladder = []
for i in range(h) :
    for j in range(n-1) :
        if arr[i][j] == 0 and arr[i][j+1] == 0 : # 사다리를 놓은 수 있는 경우
            ladder.append((i,j))

min_ladder = 1e9
for i in range(4) : # i : 추가 사다리 개수
    # print('추가 사다리 수 : ', i)
    if i == 0 :
        if check(arr) :
            min_ladder = min(min_ladder, i)
    else:
        for plus in combinations(ladder, i) : # 사다리 선택
            if min_ladder > i :
                tmp = m + 1
                # print('추가 사다리 위치 : ', plus)
                for r,c in plus : # 사다리 추가
                    arr[r][c] = tmp
                    arr[r][c+1] = tmp
                    tmp += 1
                if check(arr):
                    min_ladder = min(min_ladder, i)
                for r,c in plus : # 사다리 제거
                    arr[r][c] = 0
                    arr[r][c+1] = 0
                # print('사다리 수 : ', min_ladder)
                # print('=============================')

if min_ladder == 1e9 :
    print(-1)
else :
    print(min_ladder)

###################################################################
from sys import stdin

def back_tracking(n: int, max_cnt: int):
    global ladder, answer, H, N

    if answer!=-1:
        return
    
    cur_cnt = check()
    if cur_cnt+(max_cnt-n)*2 < N:
        return
    
    if n==max_cnt:
        if cur_cnt==N:
            answer = max_cnt
        return
    
    for h in range(1, H+1):
        for i in range(1, N):
            if ladder[h][i]==0 and ladder[h][i+1]==0:
                ladder[h][i], ladder[h][i+1] = i+1, i
                back_tracking(n+1, max_cnt)
                ladder[h][i], ladder[h][i+1] = 0, 0

def check() -> int:
    global ladder, N, H
    matched = 0
    for i in range(1, N+1):
        cur_i = i
        for h in range(1, H+1):
            if ladder[h][cur_i]!=0:
                cur_i = ladder[h][cur_i]
        if cur_i==i:
            matched += 1
    return matched

N, M, H = map(int, stdin.readline().split())
ladder = [[0]*(N+1) for _ in range(H+1)]
for i in stdin:
    a, b = map(int, i.split())
    ladder[a][b] = b+1
    ladder[a][b+1] = b
answer = -1
for cnt in range(4):
    back_tracking(0, cnt)
    if answer != -1:
        break
print(answer)