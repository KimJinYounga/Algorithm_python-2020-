import sys

q = lambda: sys.stdin.readline().strip()
N, M = map(int, q().split())
tree = [list(map(int, list(q()))) for i in range(N)]

def solution(tree):
    answer = 1

    def BFS():
        nonlocal answer
        visited = [[0] * M for i in range(N)]
        visited[0][0]=1
        queue = [(0, 0)]
        direct = [-1, 1]
        while queue:
            # 앞뒤양옆 validation 위치를 타겟으로 잡고 visited에는 target을 append <or> **visited를 0으로 초기화시키고 방문할때마다 1로 바꿔줌**
            if visited[N - 1][M - 1] == 1:
                return 0
            # 위치가 - or +인지 검사(다시)
            que_len = len(queue)
            for _ in range(que_len):
                x, y = queue.pop(0)  # target = (0,0)

                for i in direct:
                    if x + i >= 0 and x + i < N and tree[x + i][y] == 1 and visited[x + i][y] == 0:
                        queue.append((x + i, y))
                        visited[x+i][y]=1
                    if y + i >= 0 and y + i < M and tree[x][y + i] == 1 and visited[x][y + i] == 0:
                        queue.append((x, y + i))
                        visited[x][y+i] = 1
            answer += 1

    BFS()
    return answer


print(solution(tree))
