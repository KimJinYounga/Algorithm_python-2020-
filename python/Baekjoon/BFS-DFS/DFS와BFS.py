from sys import stdin

n, m, v = map(int, stdin.readline().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    line = list(map(int, stdin.readline().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1


def BFS(start):
    queue = [start]
    bfs_visited = [start]
    while queue:
        target = queue.pop(0)
        for i, v in enumerate(matrix[target]):
            if v == 1 and i not in bfs_visited:
                queue.append(i)
                bfs_visited.append(i)

    return bfs_visited


def DFS(start, dfs_visited):
    dfs_visited.append(start)
    for i, v in enumerate(matrix[start]):
        if v == 1 and i not in dfs_visited:
            DFS(i, dfs_visited)
    return dfs_visited


print(*DFS(v, []))
print(*BFS(v))