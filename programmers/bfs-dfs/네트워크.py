n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]


def solution(n, computers):
    answer = 0
    arr = [i for i in range(n)]
    while arr:
        for i in dfs(arr[0], []):
            arr.remove(i)
        answer += 1
    return answer


def dfs(start, visited):
    visited.append(start)
    for i, v in enumerate(computers[start]):
        if v == 1 and i not in visited:
            dfs(i, visited)
    return visited


print(solution(n, computers))
