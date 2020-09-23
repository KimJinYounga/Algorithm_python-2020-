N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True
    return False


count = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1

print(count)
