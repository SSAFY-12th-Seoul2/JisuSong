N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N
min_diff = 100*2*N

def dfs(n, idx) :
    global min_diff
    if n == N//2 :
        s1 = 0
        s2 = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j] :
                    s1 += ab[i][j]
                elif not visited[i] and not visited[j] :
                    s2 += ab[i][j]
        min_diff = min(min_diff, abs(s1-s2))
    for i in range(idx,N) :
        if not visited[i] :
            visited[i] = 1 
            dfs(n+1,i+1)
            visited[i] = 0
dfs(0,0)
print(min_diff)