arr = [[0]*100 for _ in range(100)]
for _ in range(4) :
    x1, y1, x2, y2 = map(int, input().split()) # 직사각형 좌표
    for x in range(x1, x2) :
        for y in range(y1, y2) :
            arr[x][y] = 1
print(sum([row.count(1) for row in arr]))
