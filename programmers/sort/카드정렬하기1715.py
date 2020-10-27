import heapq

N = int(input())
card = []
for i in range(N):
    heapq.heappush(card, int(input()))
_sum = 0

while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    target = a + b
    _sum += target
    heapq.heappush(card, target)

print(_sum)