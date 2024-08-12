# N = int(input())

# light = list(map(int, input().split()))
# n = int(input())

# for _ in range(n) :
#     gen, num = map(int, input().split())
#     if gen == 1:
#         for i in range(num-1, N, num):
#             if light[i] == 0 :
#                 light[i] = 1
#             else :
#                 light[i] = 0

#     else :
#         light[num-1] = (light[num-1] + 1)%2
#         k = 1
#         while 0 <= num - 1 - k < len(light) and 0 <= num - 1 + k < len(light):
#             if light[num-1-k] == light[num-1+k]:
#                 if light[num - 1 - k] == 0:
#                     light[num - 1 - k] = 1
#                     light[num - 1 + k] = 1
#                 else:
#                     light[num - 1 - k] = 0
#                     light[num - 1 + k] = 0
#                 k += 1
#             else :
#                 break

# for i in range(len(light)):
#     print(light[i], end=" ")
#     if (i+1) % 20 == 0:
#         print()

#########################################################

N = int(input())

light = list(map(int, input().split()))
n = int(input())

for _ in range(n) :
    gen, num = map(int, input().split())
    if gen == 1:
        for i in range(num-1, N, num):
            if light[i] == 0 :
                light[i] = 1
            else :
                light[i] = 0
    else :
        light[num-1] = (light[num-1] + 1)%2
        for k in range(1,num) :
            if num-1+k >= len(light):
                break
            if light[num-1-k] == light[num-1+k] :
                if light[num-1-k] == 0:
                    light[num-1-k] = 1
                    light[num-1+k] = 1
                else:
                    light[num-1-k] = 0
                    light[num-1+k] = 0
            else :
                break
for i in range(len(light)) :
    print(light[i], end=" ")
    if (i+1) % 20 == 0 :
        print()