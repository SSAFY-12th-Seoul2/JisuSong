T = int(input())
num = list(map(int, input().split()))
line = [1]

for i in range(1, len(num)) :
    line.insert(len(line)-num[i], i+1)

print(*line)
