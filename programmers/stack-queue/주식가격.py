from collections import deque

prices = [1,2,3,2,3]
def solution(prices):
    prices = deque(prices)
    answer = []
    long = len(prices)
    for i in range(long):
        second = 0
        target = prices.popleft()
        for j in prices:
            second += 1
            if target > j:
                break

        answer.append(second)
    return answer

print(solution(prices))