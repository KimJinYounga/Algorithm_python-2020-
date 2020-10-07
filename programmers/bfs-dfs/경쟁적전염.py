from collections import deque

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]


def virus(target, seconds, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if arr[nx][ny] == 0:
                arr[nx][ny] = target
                q.append([target, seconds + 1, nx, ny])


data = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            data.append([arr[i][j], 0, i, j])
data.sort()
q = deque(data)

while q:
    target, seconds, x, y = q.popleft()
    if seconds == S:
        break
    virus(target, seconds, x, y)

print(arr[X - 1][Y - 1])
