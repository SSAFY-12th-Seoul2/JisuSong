def isbingo(bing) :
    bing_num = 0
    for row in bing :
        if sum(row) == 0 :
            bing_num += 1

    new = list(zip(*bing)) # 전치행렬
    for row in new :
        if sum(row) == 0 :
            bing_num += 1

    # 대각선
    if sum([bing[i][i] for i in range(5)]) == 0 :
        bing_num += 1
    if sum([bing[i][4-i] for i in range(5)]) == 0:
        bing_num += 1

    return bing_num

bing = [list(map(int,input().split())) for _ in range(5)]
speak = []
for _ in range(5) :
    speak += list(map(int,input().split()))

bing_num = 0 # 빙고 횟수
cnt = 0 # 숫자 부른 횟수
while bing_num < 3: # 빙고가 3번이 되기 전까지
    for i in range(5) :
        for j in range(5):
            if bing[i][j] == speak[cnt] : # 부른 숫자 자리를 0으로 변경
                bing[i][j] = 0
    bing_num = isbingo(bing)
    cnt += 1
    # print(cnt, bing_num)

print(cnt)