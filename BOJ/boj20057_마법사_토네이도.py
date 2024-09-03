n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def move(x):
    diffuse = [
             [0, 0, 0.02, 0, 0],
             [0, 0.1, 0.07, 0.01, 0],
             [0.05, 0, 0, 0, 0],
             [0, 0.1, 0.07, 0.01, 0],
             [0, 0, 0.02, 0, 0]]
    if x==0:
        return diffuse
    if x==1:
        return list(zip(*diffuse))[::-1]
    if x==2:
        return [d[::-1] for d in diffuse]
    if x==3:
        return list(zip(*diffuse))


r, c = n//2, n//2 # 시작 지점
dir = [[0,-1],[1,0],[0,1],[-1,0]]
d = 0 # 토네이도 이동방향, 처음에는 서쪽부터 시작
cn = 1
ans = 0 # 격자 밖 모래
while cn < 4*(n//2)+2 : # 전체를 다 돌 때까지
    cnt = min((cn+1)//2, n-1)  # 몇번 갈지 설정, 1, 1, 2, 2, 3, 3, 4, 4, ...
    mul = move(d)  # d 방향의 확산 정보
    for _ in range(cnt) : # 이동
        r, c = r + dir[d][0], c + dir[d][1]  # 위치 r, c 에서 이동, 현재 r,c 는 y
        sand = arr[r][c] # y의 모래양
        minus = 0 # 줄어든 모래양
        for i in range(5): # 모래 이동
            for j in range(5) :
                if 0<= r+i-2 < n and 0<= c+j-2 < n : # 격자 내이면
                    arr[r+i-2][c+j-2] += int(sand*mul[i][j]) # 모래 확산
                else :
                    ans += int(sand*mul[i][j]) # 격자 밖으로
                minus += int(sand*mul[i][j])

        # 알파자리
        if 0<= r + dir[d][0] < n and 0 <= c + dir[d][1] < n:
            arr[r + dir[d][0]][c + dir[d][1]] += (sand-minus)
        else :
            ans += (sand-minus)

        arr[r][c] = 0 # y에는 더 이상 모래가 없음
    d = (d+1)%4 # 방향 변경
    cn += 1
print(ans)