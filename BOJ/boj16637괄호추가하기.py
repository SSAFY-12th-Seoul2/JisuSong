def cal(num1, num2, op):
    if op == '+' :
        return num1 + num2
    elif op == '-' :
        return num1 - num2
    elif op == '*' :
        return num1 * num2

def find_max(op_idx,s) :
    global max_val
    if op_idx >= n :
        max_val = max(max_val, s)
        return
    # 괄호 추가 X
    find_max(op_idx + 2 , cal(s, int(f[op_idx+1]), f[op_idx]))

    # 괄호 추가 0
    if op_idx + 3 < n :
        find_max(op_idx+4, cal(s,cal(int(f[op_idx+1]), int(f[op_idx+3]), f[op_idx+2]), f[op_idx]))

# 입력
n = int(input())
f = list(input())
max_val = -1e9
find_max(1, int(f[0]))
print(max_val)