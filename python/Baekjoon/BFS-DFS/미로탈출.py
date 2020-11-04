from collections import deque

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, visited):
    cnt = 0
    q = deque()
    q.append([x, y])
    while q:
        if visited[N - 1][M - 1] == 1:
            break
        len_q = len(q)
        cnt += 1
        for i in range(len_q):
            a, b = q.popleft()
            if arr[a][b] == 1 and visited[a][b] == 0:
                visited[a][b] = 1
                for i in range(4):
                    nx = a + dx[i]
                    ny = b + dy[i]
                    if nx >= 0 and nx < N and ny >= 0 and ny < M:
                        q.append([nx, ny])

    return cnt


visited = [[0] * M for _ in range(N)]
print(bfs(0, 0, visited))
