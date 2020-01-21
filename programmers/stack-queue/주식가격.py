from collections import deque

prices = [1,2,3,2,3]
def solution(prices):
    answer = []
    long = len(prices)
    for i in range(long):
        second = 0
        target = prices.pop(0)
        for j in prices:
            second += 1
            if target > j:
                break

        answer.append(second)
    return answer

print(solution(prices))