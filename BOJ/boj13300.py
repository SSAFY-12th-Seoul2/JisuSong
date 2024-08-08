N, k = map(int, input().split())

d = {}
# 딕셔너리 생성
for _ in range(N) :
    gen, grade = map(int, input().split())
    d[(gen, grade)] = d.get((gen, grade), 0) + 1

# 딕셔너리 순회
bang = 0
for key, v in d.items() :
    bang += v//k # 방배정
    if v%k != 0 : # 남은 인원있으면
        bang += 1 # 방 1개 추가
print(bang)