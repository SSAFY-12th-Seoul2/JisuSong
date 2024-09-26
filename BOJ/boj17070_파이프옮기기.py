import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# cnt = 0
memo = {}

def dfs(state,r,c):
    cnt = 0
    if  r == n-1 and c == n-1 : # 끝에 도달
        return 1

    if (state,r,c) in memo :
        return memo[state,r,c]

    if state == 'garo':
        if 0<= r < n and 0<= c+1 < n and arr[r][c+1] == 0 :
            cnt += dfs('garo', r, c+1)
        if 0 <= r + 1 < n and 0 <= c + 1 < n and arr[r][c + 1] == 0 and arr[r + 1][c] == 0 and arr[r + 1][c + 1] == 0:
            cnt += dfs('dia', r+1, c+1)
    elif state == 'sero':
        if 0 <= r + 1 < n and 0 <= c < n and arr[r + 1][c] == 0:
            cnt += dfs('sero', r+1, c)
        if 0 <= r + 1 < n and 0 <= c + 1 < n and arr[r][c + 1] == 0 and arr[r + 1][c] == 0 and arr[r + 1][c + 1] == 0:
            cnt += dfs('dia', r+1, c+1)
    else :
        if 0 <= r < n and 0 <= c + 1 < n and arr[r][c + 1] == 0:
            cnt += dfs('garo', r, c+1)
        if 0 <= r + 1 < n and 0 <= c < n and arr[r + 1][c] == 0:
            cnt += dfs('sero', r+1, c)
        if 0 <= r + 1 < n and 0 <= c + 1 < n and arr[r][c + 1] == 0 and arr[r + 1][c] == 0 and arr[r + 1][c + 1] == 0:
            cnt += dfs('dia', r+1, c+1)

    memo[(state,r,c)] = cnt

    return cnt

print(dfs('garo',0,1))
