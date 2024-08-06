## 별 > 동그라미 > 네모 > 세모 : 4 > 3 > 2 > 1

############## 방법 1 ##############
T = int(input())

for tc in range(1,T+1) :
  A = list(map(int, input().split()))[1:] # 개수 정보 이용 안함
  B = list(map(int, input().split()))[1:]
  A.sort(reverse=True) # 거꾸로 정렬
  B.sort(reverse=True)
  while A or B : # A와 B가 둘 중 하나라도 존재할 때
    if not A : # A 행렬이 없으면
        print('B')
        break
    elif not B : # B 행렬이 없으면
        print('A')
        break
    else : # 둘 다 있으면
        a, b = A.pop(0), B.pop(0) # 첫번째 pop
        if a > b : # a가 크면
            print('A')
            break
        elif a < b : # b가 크면
            print('B')
            break
        # 둘이 같으면 while 반복, 단, 둘 다 빈 행렬이라면 무승부
        if A == [] and B == [] : 
            print('D')

############## 방법 2 ##############
T = int(input())

for tc in range(1,T+1) :
    A = list(map(int, input().split()))[1:] # 개수 정보 이용 안함
    B = list(map(int, input().split()))[1:]
    
    for i in range(4,0,-1) :
        cnt_a = A.count(i) 
        cnt_b = B.count(i)
        if cnt_a > cnt_b :
            print('A')
            break
        elif cnt_a  < cnt_b:
            print('B')
            break
        if i == 1 and cnt_a == cnt_b : # 마지막 도형까지 개수가 같다면
            print('D')
            break