T = int(input())
arr = [[0]*100 for _ in range(100)] # 도화지 전체
for _ in range(1, T + 1):
    x, y = map(int, input().split())
    for i in range(y,y+10): # 해당하는 칸 1로 변경
        arr[i][x:x+10] = [1]*10

print(sum([sum(row) for row in arr])) # 1의 개수 == 면적