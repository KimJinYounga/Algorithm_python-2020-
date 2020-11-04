N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_result = 1000000000
max_result = 1000000000 * (-1)
result = 0


def dfs(i, target):
    global add, sub, mul, div, min_result, max_result
    if i == N:
        min_result = min(min_result, target)
        max_result = max(max_result, target)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, target + numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, target - numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, target * numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(target / numbers[i]))
            div += 1

    return [max_result, min_result]


for i in dfs(1, numbers[0]):
    print(i)
