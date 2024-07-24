## 10163 색종이
arr = [list(0 for _ in range(1001)) for _ in range(1001)]
T = int(input())

for t in range(1,T+1) :
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w) :
        arr[i][y:y+h] = [t]*h
        
for i in range(1, T+1):
    print(sum([row.count(i) for row in arr]))