N, M, x, y, K = map(int, input().split())

Map = [list(map(int, input().split())) for j in range(N)]

directions = list(map(int, input().split()))

# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


class Dice:
    def __init__(self, x, y, top, bottom, e, w, n, s):
        self.x = x
        self.y = y
        self.top = top
        self.bottom = bottom
        self.e = e
        self.w = w
        self.n = n
        self.s = s


def move(dice, d):
    nx = dice.x + dx[d]
    ny = dice.y + dy[d]

    if nx >= 0 and nx < N and ny >= 0 and ny < M:
        dice.x = nx
        dice.y = ny

        # 동 서 북 남
        if d == 0:
            dice.top, dice.bottom, dice.w, dice.e = dice.e, dice.w, dice.top, dice.bottom
        elif d == 1:
            dice.top, dice.bottom, dice.w, dice.e = dice.w, dice.e, dice.bottom, dice.top
        elif d == 2:
            dice.top, dice.bottom, dice.s, dice.n = dice.s, dice.n, dice.bottom, dice.top
        else:
            dice.top, dice.bottom, dice.s, dice.n = dice.n, dice.s, dice.top, dice.bottom

        if Map[dice.x][dice.y] == 0:
            Map[dice.x][dice.y] = dice.bottom
        else:
            dice.bottom = Map[dice.x][dice.y]
            Map[dice.x][dice.y] = 0
        return True
    else:
        return False


def solve(x, y, directions):
    dice = Dice(x, y, 0, 0, 0, 0, 0, 0)

    for i in directions:
        if move(dice, i - 1) == True:
            print(dice.top)


solve(x, y, directions)
