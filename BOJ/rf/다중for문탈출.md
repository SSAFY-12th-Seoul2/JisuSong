## boj2309

### | 다중 for문 탈출하기

#### ① 함수 내부의 return을 통한 반복문 탈출
```python
dw = [int(input()) for _ in range(9)]
d = sum(dw) - 100

def seven(dw) :
    for i in range(len(dw)-1) :
        for j in range(i+1, len(dw)) :
            if dw[i] + dw[j] == d :
                dw.pop(i)
                dw.pop(j-1)
                return  

dw.sort()
for i in dw :
    print(i)
```

#### ② flag를 활용한 다중 반복문 탈출
```python
dw = [int(input()) for _ in range(9)]
d = sum(dw) - 100
flag = 0

for i in range(len(dw)-1) :
    if flag == 1 :
        break

    for j in range(i+1, len(dw)) :
        if dw[i] + dw[j] == d :
            dw.pop(i)
            dw.pop(j-1)
            flag = 1
            break

dw.sort()

for i in dw :
    print(i)
```

#### ③ 에러 발생을 통한 다중 반복문 탈출
> try-catch문을 통해 에러를 발생시켜 다중 반복문을 쉽게 탈출할 수 있습니다. 

> 루프를 탈출하도록 돕는 에러를 미리 정의한 후, 특정 조건을 만족하면 해당 에러를 발생시킵니다. 

> 그러면 에러 발생으로 except문을 실행하게 되고, except문에서는 아무 일도 하지 않기 때문에 다중 반복문을 나갈 수 있습니다.

```python
dw = [int(input()) for _ in range(9)]
d = sum(dw) - 100

try : 
    for i in range(len(dw)-1) :
        for j in range(i+1, len(dw)) :
            if dw[i] + dw[j] == d :
                dw.pop(i)
                dw.pop(j-1)
                raise

except :
    pass

dw.sort()

for i in dw :
    print(i)
```