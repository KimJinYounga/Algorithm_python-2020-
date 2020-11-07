from collections import defaultdict
import sys

N = int(sys.stdin.readline())
_dict = defaultdict(int)
q = []
answer = []
_sum = 0
for i in range(N):
    target = int(sys.stdin.readline())
    _dict[target] += 1
    _sum += target
    q.append(target)
q = sorted(q)
_items = list(_dict.items())
_items = sorted(_items, key=lambda x: x[0])
_items = sorted(_items, key=lambda x: x[1], reverse=True)
freq = 0
if len(_items) > 1:
    if _items[0][1] == _items[1][1]:
        freq = _items[1][0]
    else:
        freq = _items[0][0]
else:
    freq = _items[0][0]

# round() : 반올림 함수
answer = [round(_sum / N), q[N // 2], freq, q[-1] - q[0]]

for i in answer:
    print(i)

