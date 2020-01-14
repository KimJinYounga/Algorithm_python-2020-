from collections import deque
from functools import reduce

bridge_length=2
weight=10
truck_weights=	[7,4,5,6]

# 에러해결 : dictionary는 중복을 허용하지 않기때문 -> ing 를 딕션에서 리스트로 바꿈

def solution(bridge_length, weight, truck_weights):
    ing = []
    end = []
    time=0
    long=len(truck_weights)

    # 전부 다리를 건너올 때까지 while loop
    while long != len(end):
        time+=1

        # 다리위에서 1초씩 움직임
        for i in ing:
            i[1]+=1

        # 다리를 다 건너면 end리스트로 넘기고 ing리스트에선 삭제
        for i in ing:
            if i[1]==bridge_length:
                end.append(ing.pop(0)[0])
                break


        # 다리를 건너는 트럭 리스트 구하기
        if len(truck_weights)!=0:
            total=0
            for i in ing:
                total+=i[0]
            if total + truck_weights[0] <= weight:
                ing.append([truck_weights.pop(0), 0])

    return time

print(solution(bridge_length, weight, truck_weights))