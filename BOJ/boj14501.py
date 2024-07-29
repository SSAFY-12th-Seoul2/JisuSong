def dfs(start, day, price):
  global max_price
  if start+day > N+1 :
    return # 조건에 맞지 않으면 새로운 price 값 반영 전에 중단
  max_price = max(max_price, price)

  for i in range(start+day, N+1): # 1일 > 4일 / 1일 > 5일 ...
    dfs(i, lst[i][0], price+lst[i][1])

N = int(input()) 
lst = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]

max_price = 0
for i in range(1, N+1):
    dfs(i, lst[i][0], lst[i][1])
print(max_price)