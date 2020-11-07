from copy import deepcopy

N, M = map(int, input().split())
arr = [[0] * M for i in range(N)]
cctv_size = 0
CCTV = []
answer = 100
# 각 cctv 종류별 회전 횟수
rot_cnt = [0, 4, 2, 4, 4, 1]


def update(direction, x, y):
    direction = direction % 4
    # 동
    if direction == 0:
        for i in range(y + 1, M):
            if arr[x][i] == 6: break
            arr[x][i] = '#'

    # 북
    if direction == 1:
        for i in range(x - 1, -1, -1):
            if arr[i][y] == 6: break
            arr[i][y] = '#'

    # 서
    if direction == 2:
        for i in range(y - 1, -1, -1):
            if arr[x][i] == 6: break
            arr[x][i] = '#'

    # 남
    if direction == 3:
        for i in range(x + 1, N):
            if arr[i][y] == 6: break
            arr[i][y] = '#'


def dfs(cctv_index):
    global answer, CCTV, arr
    _min = 0
    if cctv_index == cctv_size:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    _min += 1

        if answer > _min:
            answer = _min
        return
    backup = deepcopy(arr)
    type, x, y = CCTV[cctv_index]
    for i in range(rot_cnt[type]):
        if type == 1:
            update(i, x, y)
        if type == 2:
            update(i, x, y)
            update(i + 2, x, y)
        if type == 3:
            update(i, x, y)
            update(i + 1, x, y)
        if type == 4:
            update(i, x, y)
            update(i + 1, x, y)
            update(i + 2, x, y)
        if type == 5:
            update(i, x, y)
            update(i + 1, x, y)
            update(i + 2, x, y)
            update(i + 3, x, y)

        dfs(cctv_index + 1)
        arr = deepcopy(backup)


for i in range(N):
    target = list(map(int, input().split()))
    for j in range(M):
        arr[i][j] = target[j]
        if 1 <= target[j] < 6:
            CCTV.append([target[j], i, j])
            cctv_size += 1

dfs(0)
print(answer)
