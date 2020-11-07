import sys

arr = []
for i in range(4):
    arr.append(sys.stdin.readline().strip())

K = int(sys.stdin.readline())
for i in range(K):
    number, direction = map(int, sys.stdin.readline().split())
    number -= 1

    # left 검사
    now = number
    now_direction = direction
    change_list = []
    while True:
        left = now - 1
        if left < 0:
            break
        if arr[now][-2] == arr[left][2]:
            break
        else:
            change_list.append([left, now_direction])
            now_direction *= -1
            now = left

    # right 검사
    now = number
    now_direction = direction
    while True:
        right = now + 1
        if right > 3:
            break
        if arr[now][2] == arr[right][-2]:
            break
        else:
            change_list.append([right, now_direction])
            now_direction *= -1
            now = right

    for i in change_list:
        index, now_direction = i
        arr[index] = arr[index][now_direction:] + arr[index][:now_direction]
    arr[number] = arr[number][-direction:] + arr[number][:-direction]

result = 0
for i in range(4):
    if arr[i][0] == '1':
        result += 2 ** i
print(result)