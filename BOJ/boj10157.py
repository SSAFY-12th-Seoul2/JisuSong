x, y = map(int, input().split())
s = int(input())

def find_my_seat(x,y,s,n) :
    if s <= y :
        print(n+1, n+s)  
    elif s <= x + y -1 :
        print(n+s-y+1, n+y)
    elif s <= x + 2*y -2 :
        print(n+x, n+ x + 2*y -s -1)
    else :
        print(n+ 2*x + 2*y -s -2, n+ 1)

if s > x*y :
    print(0)
    
else :
    n = 0
    while s > 2*x + 2*y - 4 :
        n += 1
        s = s -2*x -2*y + 4
        x -= 2
        y -= 2
    find_my_seat(x,y,s,n)