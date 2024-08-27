# 큐를 이용한 연합 표시
def make_g():
    g = [[0]*n for _ in range(n)] # 연합 번호 표기용
    num = 0 # 연합 번호
    num_pop = [] # 연합 번호에 해당하는 인구수
    num_cnt = [] # 연합 번호에 해당하는 국가수
    for i in range(n) :
        for j in range(n) :
            if g[i][j] == 0 : # 연합 배정이 안되어있다면
                num += 1 # 연합번호수 변경
                g[i][j] = num # 연합 번호 표기
                num_pop += [p[i][j]] # 연합 인구 추가
                num_cnt += [1] # 연합 국가 추가
                q = [(i, j)]
                while q:
                    ci, cj = q.pop(0)
                    for di, dj in [[0,1],[0,-1],[-1,0],[1,0]] :
                        ni, nj = ci+di, cj+dj
                        if 0<=ni<n and 0<=nj<n and g[ni][nj] == 0 :
                            if l <= abs(p[ci][cj]-p[ni][nj]) <= r: # 인구 차이가 L명 이상, R명 이하
                                g[ni][nj] = num # 같은 연합 번호 부여
                                num_pop[num-1] += p[ni][nj] # 인구수 추가
                                num_cnt[num-1] += 1 # 국가수 추가
                                q.append((ni, nj))

    m = [a//b for a,b in zip(num_pop, num_cnt)] # (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
    move(g, m)
    return num

# 이동
def move(g, m):
    for i in range(n) :
        for j in range(n) :
            p[i][j] = m[g[i][j]-1]

n, l, r = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
day = 0
while True :
    num = make_g()
    if num >= n*n : #모든 국가가 서로 다른 연합번호를 가짐 = 이동X
        break
    day += 1
print(day)