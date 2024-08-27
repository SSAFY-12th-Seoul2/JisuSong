def chicken(start): # depth : , start :
    global min_dis
    if len(stores) == m : # 상점의 개수가 m개인 경우
        tmp_dis = min_distance(homes,stores)
        min_dis = min(min_dis, tmp_dis)
        return

    for i in range(start, len(chicken_stores)) :
        stores.append(chicken_stores[i])
        chicken(i+1)
        stores.pop()

def distance(a,b) :
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def min_distance(homes, stores) : # 집과 가장 가까운 치킨집 거리들의 합
    total = 0
    for h in homes :
        total += min(distance(h, s) for s in stores)
    return total

## 입력
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

homes = [(i, j) for i in range(n) for j in range(n) if arr[i][j] == 1] # 집 위치
chicken_stores = [(i, j) for i in range(n) for j in range(n) if arr[i][j] == 2] # 치킨 집 위치

stores = []
min_dis = 2*n*len(homes)

chicken(0)
print(min_dis)

#################### 시간 초과 #####################
def home(): # 집 위치 파악
    global homes
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                homes.append((i,j))

def chicken(m): # m개의 치킨 집 선택 및 거리 계산
    global store, min_dis
    if len(store) == m : # 상점의 개수가 3개인 경우
        tmp_dis = min_distance(homes,store)
        if tmp_dis < min_dis :
            min_dis = tmp_dis
        return

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2 and (i,j) not in store:
                store.append((i,j))
                chicken(m)
                store.pop()

def distance(a,b) :
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def min_distance(homes,store) :
    total = 0
    for h in homes :
        t = 2*n
        for s in store :
            if t > distance(h,s):
                t = distance(h,s)
        total+=t
    return total

## 입력

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

store = []
homes = []
home()
min_dis = 2*n*len(homes)
chicken(m)
print(min_dis)