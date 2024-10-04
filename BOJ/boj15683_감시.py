N, M = map(int,input().split()) # 사무실크기 N*M
office = [0 for _ in range(N)]
cctv = []
dx, dy = [-1,0,1,0],[0,1,0,-1] # 상 우 하 좌 (시계방향)

for i in range(N):
    office[i] = list(map(int, input().split()))
    for j in range(M):
        if office[i][j] in [1,2,3,4,5]:
            cctv.append([i,j,office[i][j]])

cctv = sorted(cctv, key=lambda x: x[2], reverse=True)

def check(x,y,d):
    global N, M, office
    while(True):
        xx,yy = x+dx[d],y+dy[d]
        if xx < 0 or xx >= N or yy < 0 or yy >= M or office[xx][yy] == 6:
            break
        elif office[xx][yy] == 0:
            office[xx][yy] = '#'
        x, y = xx, yy

def count(x,y,d):
    global N, M, office
    count = 0
    while(True):
        xx,yy = x+dx[d],y+dy[d]
        if xx < 0 or xx >= N or yy <0 or yy >= M or office[xx][yy] == 6:
            break
        elif office[xx][yy] == 0:
            count += 1
        x, y = xx, yy
    return count

for cam in cctv:
    x, y, n = cam[0],cam[1],cam[2]
    if n == 5:
        check(x,y,0)
        check(x,y,1)
        check(x,y,2)
        check(x,y,3)        
    elif n == 1:
        temp,d = 0,0
        for i in range(4):
            if count(x,y,i)>temp:
                d = i
                temp = count(x,y,d)
        check(x,y,d)
    elif n == 2:
        if count(x,y,0)+count(x,y,2) > count(x,y,1)+count(x,y,3): # 상하 좌우
            d1, d2 = 0,2
        else:
            d1, d2 = 1,3 
        check(x,y,d1)
        check(x,y,d2)
    elif n == 3:
        temp,d1,d2 = 0,0,1
        for i in range(4):
            j = (i+1)%4
            if count(x,y,i)+count(x,y,j) > temp:
                d1, d2= i,j
                temp = count(x,y,d1)+count(x,y,d2)
        check(x,y,d1)
        check(x,y,d2)
    elif n == 4:
        temp,d = 1e9,0
        for i in range(4):
            if count(x,y,i) < temp:
                d = i
                temp = count(x,y,d)
        for j in range(4):
            if j != d:
                check(x,y,j)

answer = 0
for i in range(N):
    for j in range(M):
        if office[i][j] == 0:
            answer += 1

print(answer)  