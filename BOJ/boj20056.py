def moving(k, lst) :
    r, c = k[0], k[1]
    for i in range(0, len(lst)//3) :
        m, s, d = lst[3*i], lst[3*i+1], lst[3*i+2]
        nr, nc = (r + s*dir[d][0])%n, (c + s*dir[d][1])%n # 방향 di로 속력 si칸 만큼 이동
        new[(nr, nc)] = new.get((nr,nc), []) + [m,s,d]

def fireball(k, new):
    v = new.pop(k)
    if len(v) > 3:  # 두개 이상의 파이어볼이 있는 칸에서
        tmp_m = int(sum(v[0:len(v):3]) / 5)  # 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
        if tmp_m == 0 :
            return # 질량이 0인 파이어볼은 소멸되어 없어진다.
        tmp_s = int(sum(v[1:len(v):3]) / (len(v) / 3))  # 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
        even = odd = 0
        for i in range(len(v) // 3):
            if v[2 + 3 * i] % 2 == 0:
                even += 1
            else:
                odd += 1
        if even == len(v)//3 or odd == len(v)//3: # 파이어볼의 방향이 모두 홀수이거나 모두 짝수
            tmp_d = [0, 2, 4, 6]
        else:
            tmp_d = [1, 3, 5, 7]
        for j in range(4):  # 파이어볼은 4개의 파이어볼로 나누어진다.
            new[k] = new.get(k, []) + [tmp_m, tmp_s, tmp_d[j]]
    else: # 한 개인 경우 되돌려놓기
        new[k] = v

n, m, k = map(int, input().split())
dir = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
info = {}
for _ in range(m) :
    r,c,m,d,s = map(int, input().split())
    info[(r-1,c-1)] = [m,d,s] # 키 값 : 위치, value : 질량 방향 속도

for _ in range(k) :
    new = {}
    for k, v in info.items():
        moving(k,v)
    # 이동이 모두 끝난 뒤
    keys = list(new.keys())
    for k in keys : # 딕셔너리 순회하며
        fireball(k, new)
    info = new

# 남은 질량의 합 구하기
ans = 0
for k, v in info.items() :
    ans += sum(v[0:len(v):3])
print(ans)