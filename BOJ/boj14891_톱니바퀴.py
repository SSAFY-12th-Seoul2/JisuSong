wheel = [list(map(int, input())) for _ in range(4)]
n = int(input())

def s(wheel, spin) :
    new_wheel = []
    for w, d in zip(wheel, spin) :
        if d == -1 : # 반시계 방향
            new_wheel += [w[1:] + [w[0]]]
        elif d == 1 : # 시계 방향
            new_wheel += [[w[-1]] + w[:-1]]
        elif d == 0 :
            new_wheel += [w]
    return new_wheel

for i in range(n) :
    spin = [0,0,0,0] # 회전 방향을 담을 리스트
    idx, d = map(int, input().split()) # 회전할 바퀴, 방향
    spin[idx-1] = d
    q = [(idx-1,d)] # 큐에 삽입
    visited = [0,0,0,0]
    visited[idx-1] = 1

    while q : # 큐가 존재할 때까지
        idx, d = q.pop(0) # 큐에서 팝
        if idx - 1 >= 0 and visited[idx-1] == 0 and wheel[idx-1][2] != wheel[idx][6] : # 왼쪽 바퀴와 맞닿은 부분이 서로 다르면
            spin[idx-1] = -d # 회전 방향 정보 저장
            q.append((idx-1,-d))# 큐에 삽입
            visited[idx - 1] = 1

        if idx + 1 < 4 and visited[idx+1] == 0and wheel[idx][2] != wheel[idx+1][6]:  # 오른쪽 바퀴와 맞닿은 부분이 서로 다르면
            spin[idx+1] = -d  # 회전 방향 정보 저장
            q.append((idx+1, -d))  # 큐에 삽입
            visited[idx + 1] = 1

    # 회전
    wheel = s(wheel, spin)

# 점수산출
score = 0
for i in range(4) :
    if wheel[i][0] == 1 :
        score += 2**(i)

print(score)