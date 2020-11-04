from collections import deque

# deque를 사용하여 실행 시간 줄임
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

