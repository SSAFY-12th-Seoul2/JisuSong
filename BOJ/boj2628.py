m, n = map(int, input().split())
w, l = [0], [0]
T = int(input())

for _ in range(T) :
  a, b = map(int, input().split())

  if a == 1 :
    w.append(b)
  else :
    l.append(b)
w = w + [m]
l = l + [n]

w.sort()
l.sort()

max_w = 0
max_l = 0
    
for x,y in zip(w[:-1], w[1:]) :
  if max_w < y-x :
    max_w = y-x
  
for x,y in zip(l[:-1], l[1:]) :
  if max_l < y-x :
    max_l = y-x
    
print(max_w * max_l)
