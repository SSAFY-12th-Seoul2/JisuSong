import copy
# 회전 연산 정보에 따라 회전한 어레이를 리턴하는 함수
def spin(s, origin) : # s : 회전 연산 정보, arr=회전할 어레이
    r, c, s = s
    x1,y1,x2,y2 = r-s-1, c-s-1, r+s-1, c+s-1
    tmp_arr = copy.deepcopy(origin)
    for _ in range(s) :
        tmp_arr[x1][y1+1:y2+1] = origin[x1][y1:y2]
        tmp_arr[x2][y1:y2] = origin[x2][y1+1:y2+1]
        for x in range(x1, x2) :
            tmp_arr[x][y1] = origin[x+1][y1]
        for x in range(x1+1,x2+1):
            tmp_arr[x][y2] = origin[x-1][y2]
        x1, y1, x2, y2 = x1+1, y1+1, x2-1, y2-1
    return tmp_arr

# 합을 구하는 함수
def min_sum_row(arr) :
    global min_sum
    for row in arr :
        if min_sum > sum(row) :
            min_sum = sum(row)


def permutation(d, k) :
    if d == k :
        orders.append(perm[:])
        return perm
    for i in range(k) :
        if visited[i] == 0 :
            visited[i] = 1
            perm.append(i)
            permutation(d+1,k)
            perm.pop()
            visited[i] = 0

n, m, k = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
s = [list(map(int, input().split())) for _ in range(k)]
min_sum = 100*m


# 가능한 순서 파악
visited = [0]*k
perm = []
orders = []
permutation(0, k)
for order in orders:
    origin = copy.deepcopy(arr)
    # 회전
    for i in order:
        origin = spin(s[i], origin)
    # 합
    min_sum_row(origin)
print(min_sum)