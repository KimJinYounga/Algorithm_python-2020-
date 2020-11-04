N = int(input())
K = int(input())
apple = []
for i in range(K):
    apple.append(list(map(int, input().split())))
L = int(input())
snake = []
for i in range(L):
    X, C = input().split()
    snake.append([int(X), C])
board = [[0] * N for _ in range(N)]
for i in apple:
    x, y = i
    board[x - 1][y - 1] = 1

# [동, 남, 서, 북]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 뱀 몸통이 있는 부분
body = []
count = 0
direction = 0
head_x = 0
head_y = 0

while True:
    if len(snake) != 0:
        X, C = snake[0]
        if X == count:
            snake.pop(0)
            if C == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
    # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    body.append([head_x, head_y])
    board[head_x][head_y] = 2
    head_x += dx[direction]
    head_y += dy[direction]

    if head_x == N or head_y == N or head_x == -1 or head_y == -1:
        break
    if board[head_x][head_y] == 2:
        break
    # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if board[head_x][head_y] == 1:
        board[head_x][head_y] = 0
    # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    else:
        tail_x, tail_y = body.pop(0)
        board[tail_x][tail_y] = 0
    count += 1

print(count + 1)
