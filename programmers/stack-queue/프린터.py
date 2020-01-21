from collections import deque
priorities=[3,3,4,2]
location=2

def solution(priorities, location):
    answer = 0
    # 1. [우선순위, 인덱스]를 저장할 2차원 배열 printer 선언
    printer = [[v,i] for i,v in enumerate(priorities)]
    printer = deque(printer)

    # 2. printer 배열에서 우선순위에 따라 printed배열로 넘기기
    printed = []

    while(len(printer)!=0):
        current_doc, index = printer[0]

        # 배열에서 가장 큰 원소일 경우, printer.pop(0) -> printed배열
        if current_doc == max(printer)[0]:
            printed.append(printer.popleft())

        for i in printer:
            if current_doc < i[0]:
                printer.append(printer.popleft())
                break

    # 3. location에 해당하는 '인덱스+1' return
    for i in printed:
        if i[1] == location:
            answer = printed.index(i)+1
    return answer

print(solution(priorities, location))