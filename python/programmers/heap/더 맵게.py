import heapq

"""
heapq ==> heapq.heappush()를 하면 자동정렬됌(asc)
"""
scoville=[1,2,3]
K=7

def solution(scoville, K):
    answer=0
    heap = sorted(scoville)

    while heap[0]<K:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, first + second *2)
        answer+=1
        if len(heap)==1:
            if heap[0] < K:
                return -1
    return answer


print(solution(scoville,K))