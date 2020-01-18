priorities=[2, 1, 3, 2]
location=2


def solution(priorities, location):
    answer = 0
    # 1. [우선순위, 인덱스]를 저장할 2차원 배열 printer 선언
    printer = [[v,i] for i,v in enumerate(priorities)]
    # 2. printer 배열에서 우선순위에 따라 재배열
    running=True
    while(running):
        if len(list(set(priorities))) ==1:
            running=False

        current_doc, index = printer[0]
        for i in printer:
            if current_doc < i[0]:
                printer.append(printer.pop(0))
                break
        # 에러남 : priorities가 모두 같을 경우.

        if index == max(printer)[1]:
            running = False

    # 3. location에 해당하는 '인덱스+1' return
    for i in printer:
        if i[1] == location:
            answer = printer.index(i)+1
    return answer

print(solution(priorities, location))