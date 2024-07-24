dw = [int(input()) for _ in range(9)]
d = sum(dw) - 100

def seven(dw) :
    for i in range(len(dw)-1) :
        for j in range(i+1, len(dw)) :
            if dw[i] + dw[j] == d :
                dw.pop(i)
                dw.pop(j-1)
                return dw 
dw = seven(dw)
dw.sort()
for i in dw :
    print(i)
