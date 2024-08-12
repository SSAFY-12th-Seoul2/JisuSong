for _ in range(4) :
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 공통X : y1 > q2 / q1 < y2 / p1 < x2 / x1 > p2
    if y1 > q2 or q1 < y2 or p1 < x2 or x1 > p2  :
        print('d')
    # 점 : (x1,y1) == (p2, q2) / (p1,y1) == (x2, q2) / (p1,q1) == (x2, y2) / (x1,q1) == (p2, y2)
    elif (x1,y1) == (p2, q2) or (p1,y1) == (x2, q2) or (p1,q1) == (x2, y2) or (x1,q1) == (p2, y2) :
        print('c')
    # 선분 : y1 == q2 / q1 == y2 / p1 == x2 / x1 == p2
    elif y1 == q2 or q1 == y2 or p1 == x2 or x1 == p2 :
        print('b')
    else :
        print('a')