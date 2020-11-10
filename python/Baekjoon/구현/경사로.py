import sys

N, L = map(int, sys.stdin.readline().split())
Map = [[0] * N for _ in range(N)]
result = 0
for i in range(N):
    Map[i] = list(map(int, sys.stdin.readline().split()))

# 가로 : Map[0][0], Map[0][1],,, Map[0][N-1]
for i in range(N):
    target = Map[i][0]  # 현재 칸의 높이
    _cnt = 1  # 높이가 같은 연속된 칸의 개수
    j = 1
    running = True
    while running:
        _diff = Map[i][j] - target  # 옆 칸과의 높이 차이
        if _diff == 0:  # 높이가 같을 때
            _cnt += 1
            target = Map[i][j]
        elif _diff == 1 and _cnt >= 0:  # 높이가 다를때, 사다리를 놓을 수 있는 경우
            if _cnt < L:  # 사다리를 놓을 수 없는 경우
                running = False
                break
            _cnt = 1  # 사다리를 놓을 수 있 경우
            target = Map[i][j]
        elif _diff == -1 and _cnt >= 0:
            _cnt = -L + 1
            target = Map[i][j]
        else:
            running = False
            break
        j += 1
        if j == N:
            if _cnt >=0: result += 1
            running = False
            break

for j in range(N):
    target = Map[0][j]  # 현재 칸의 높이
    _cnt = 1  # 높이가 같은 연속된 칸의 개수
    i = 1
    running = True
    while running:
        _diff = Map[i][j] - target  # 옆 칸과의 높이 차이

        # 3 2 2 1 1 1 인 경우 처리방법 생각하기..

        if _diff == 0:  # 높이가 같을 때
            _cnt += 1
        elif _diff == 1 and _cnt >= 0:  # 사다리를 놓을 수 있는 경우
            if _cnt < L:
                running = False
                break
            _cnt = 1
            target = Map[i][j]
        elif _diff == -1 and _cnt >= 0:
            _cnt = -L + 1
            target = Map[i][j]
        else:
            running = False
            break

        i += 1
        if i == N:
            if _cnt >= 0: result += 1
            running = False
            break

print(result)
