M = 1000000
tmp = [False]*2 + [True]*(M-1)
for i in range(2,M+1):
    if tmp[i]:
        for j in range(i*i, M+1, i):
            tmp[j] = False

T = int(input())

for _ in range(T) :
    N = int(input())
    ans = 0
    for i in range(int(N/2)+1) :
        if tmp[i] and tmp[N-i] :
            ans += 1
    print(ans)