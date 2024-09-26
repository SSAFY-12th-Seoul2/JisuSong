from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split())) # 내구도
robot = deque() # 로봇의 위치
cnt = 0 # 내구도 0인 개수

while arr.count(0) < k :
    cnt += 1

    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    arr = [arr[-1]] + arr[:-1]
    for i in range(len(robot)) :
        robot[i] = (robot[i] + 1) % (2 * n)

    if (n-1) in robot : # 로봇이 내리는 곳에 도달
        robot.remove(n-1)

    # 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    if robot : # 로봇이 있다면
      for _ in range(len(robot)) :
        r = robot.popleft() # 가장 먼저 벨트에 올라간 로봇부터
        if (r+1)%(2*n) not in robot and arr[(r+1)%(2*n)] >= 1 : # 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
          if r+1 != n-1 : # 로봇이 내리는 곳이 아닌 경우
            robot.append(r+1)
          arr[(r+1)%(2*n)] -= 1 # 이동하려는 칸의 내구도는 1 감소한다.
        else : # 만약 이동할 수 없다면 가만히 있는다
          robot.append(r)

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if arr[0] >= 1 :
      robot.append(0) # 내구도는 즉시 1만큼 감소
      arr[0] -= 1

print(cnt)

################################################################
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split())) # 내구도
robot = deque() # 로봇의 위치
cnt = 0 # 단계수
zero = 0 # 내구도 0인 개수

while zero < k :
    cnt += 1

    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    arr = [arr[-1]] + arr[:-1]
    for i in range(len(robot)) :
        robot[i] = (robot[i] + 1) % (2 * n)

    if robot and robot[0] == n-1 : # 로봇이 내리는 곳에 도달
        robot.popleft()

    # 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    if robot : # 로봇이 있다면
      for i in range(len(robot)) :
        next = (robot[i] + 1)%(2*n) # 가장 먼저 벨트에 올라간 로봇부터
        if next not in robot and arr[next] >= 1 : # 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
          robot[i] = next
          arr[next] -= 1 # 이동하려는 칸의 내구도는 1 감소한다.
          if arr[next] == 0 :
              zero += 1

    if robot and robot[0] == n-1 : # 로봇이 내리는 곳에 도달
        robot.popleft()

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if arr[0] >= 1 :
      robot.append(0)
      arr[0] -= 1 # 내구도는 즉시 1만큼 감소
      if arr[0] == 0:
        zero += 1

print(cnt)

################################################################
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))  # 내구도 배열
robots = deque([False] * (2 * n))  # 로봇의 위치 관리 (True/False)
cnt = 0  # 단계 수
zero_count = 0  # 내구도 0인 칸 개수

while zero_count < k:
    cnt += 1

    # 1. 벨트가 한 칸 회전 (로봇과 함께)
    arr = [arr[-1]] + arr[:-1]
    robots.rotate(1)  # 벨트 회전
    robots[n-1] = False  # 내리는 위치에 로봇이 있으면 내림

    # 2. 로봇 이동
    for i in range(n-2, -1, -1):  # n-1번째 위치는 내리는 곳이므로 검사할 필요 없음
        if robots[i] and not robots[i+1] and arr[i+1] > 0:
            robots[i] = False
            robots[i+1] = True
            arr[i+1] -= 1
            if arr[i+1] == 0:
                zero_count += 1

    robots[n-1] = False  # 내리는 위치에 로봇이 있으면 내림

    # 3. 올리는 위치에 로봇 올리기
    if arr[0] > 0:
        robots[0] = True
        arr[0] -= 1
        if arr[0] == 0:
            zero_count += 1

print(cnt)