numbers = [1,1,1,1,1]
target = 3

def solution(numbers, target):
    answer = 0
    len_numbers = len(numbers)
    def dfs(i):
        if i < len_numbers:
            numbers[i] *= 1
            dfs(i+1)

            numbers[i] *= -1
            dfs(i+1)

        else:
            if sum(numbers) == target:
                nonlocal answer
                answer += 1

        return answer

    dfs(0)
    return answer

print(solution(numbers, target))