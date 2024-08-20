n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]
dir = [[0,0], [0,-1], [-1,-1], [-1,0],
       [-1,1], [0,1], [1,1], [1,0], [1,-1]] #←, ↖, ↑, ↗, →, ↘, ↓, ↙
dir2 = [[1,1],[1,-1],[-1,1],[-1,-1]]

# 비바라기 시전 (N, 1), (N, 2), (N-1, 1), (N-1, 2)
cloud = [[n-1,0], [n-1,1], [n-2,0], [n-2,1]]

# 모든 구름이 di 방향으로 si칸 이동한다.
for d, mul in move :
       # print('moving_start')
       for i in range(len(cloud)) :
              r, c = cloud[i]
              r, c = (r + dir[d][0] * mul) % n, (c + dir[d][1] * mul) % n
              cloud[i] = [r,c]
              arr[r][c] += 1
       # print('=================')
       # print(arr)

       # 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다.
       for r, c in cloud:
              for dr, dc in dir2:
                     #  대각선 방향으로 거리가 1인 칸
                     nr, nc = r + dr, c + dc
                     # 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다, 물이 있는 바구니가 있다면
                     if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] > 0 :
                            arr[r][c] += 1
       # print('*****************')
       # print(arr)
       # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
       prev_cloud_set = set(map(tuple, cloud))
       new_cloud = []
       for i in range(n) :
              for j in range(n) :
                     if arr[i][j] >= 2 and (i, j) not in prev_cloud_set : # 3에서 구름이 사라진 칸이 아니어야 한다.
                            arr[i][j] -= 2
                            new_cloud += [[i,j]]
       cloud = new_cloud
       # print('##################')
       # print(arr)
       # print(cloud)
       # print()

print(sum([sum(row) for row in arr]))