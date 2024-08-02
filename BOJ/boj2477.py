## 옥수수개수
n = int(input())

## 방향과 거리를 담은 딕셔너리 생성
bat = {}
for i in range(6) :
    d , l = map(int, input().split())
    bat[d]= bat.get(d,[]) + [(i,l)] # (방향, 거리)

## 전체 면적 구하기
total = 1
max_key = []
for k, v in bat.items() :
    if len(v) == 1: # 방향에 해당하는 값이 1개면 최대 가로/세로
        total *= v[0][1]
        max_key += [k]

## 안쪽 사각형 넓이
small = 1
max_key.sort() # 가로 먼저 정렬
w_max = bat.pop(max_key[0]) # 가로 최대
l_max = bat.pop(max_key[1]) # 세로 최대

for k, v in bat.items() : # 나머지 변에 대한 정보
    if k in [1,2] : # 가로 정보 : 세로 최대와 근접변인지 
        if abs(v[0][0] - l_max[0][0]) == 1 or abs(v[0][0] - l_max[0][0]) == 5 :
            small *= v[1][1] # 근접변이면 나머지 변 곱하기
        else: 
            small *= v[0][1]
    else :
        if abs(v[0][0] - w_max[0][0]) == 1 or abs(v[0][0] - w_max[0][0]) == 5 :
            small *= v[1][1]
        else: 
            small *= v[0][1]
print(n*(total-small))