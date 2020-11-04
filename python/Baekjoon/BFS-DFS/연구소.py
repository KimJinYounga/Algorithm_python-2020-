N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
tmp = [[0] * M for _ in range(N)]
score = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def makeScore():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt


def makeWall(cnt_wall):
    if cnt_wall < 3:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    cnt_wall += 1
                    makeWall(cnt_wall)
                    arr[i][j] = 0
                    cnt_wall -= 1

    else:
        for i in range(N):
            for j in range(M):
                tmp[i][j] = arr[i][j]
        for i in range(N):
            for j in range(M):
                if tmp[i][j] == 2:
                    virus(i, j)

        global score
        score = max(score, makeScore())
        return


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus(nx, ny)


makeWall(0)
print(score)
