n, k = map(int, input().split())
temp = list(map(int, input().split()))
max_temp = -100*n
for i in range(n-k+1) :
    seq_temp = 0
    for j in range(0, k) :
        seq_temp += temp[i+j]
    max_temp = max(max_temp, seq_temp)
print(max_temp)

##############################################

n, k = map(int, input().split())
temp = list(map(int, input().split()))
max_temp = sum(temp[0:k])
crr_temp = sum(temp[0:k])
for i in range(n-k) :
    # print(temp[i],temp[i+k])
    crr_temp = crr_temp - temp[i] + temp[i+k] # 이전 합에서 앞에 제거 뒤에 추가
    if max_temp <  crr_temp :
        max_temp = crr_temp
    # print('##',max_temp)
print(max_temp)