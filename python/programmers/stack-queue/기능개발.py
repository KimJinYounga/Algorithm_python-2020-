def solution(progresses, speeds):
    answer = []
    work_day = []  # 작업일수
    sum = 1

    # a, b = divmod(first, second)
    # a = first를 second로 나눈 몫
    # b = 나머지
    for i, v in enumerate(progresses):
        a, b = divmod(100 - progresses[i], speeds[i])
        if b != 0:
            a += 1
        work_day.append(a)

    max = work_day.pop(0)
    running = True
    while (running):
        compare = work_day.pop(0)
        if max >= compare:
            sum += 1
        else:
            answer.append(sum)
            sum = 1
            max = compare

        # 마지막 인덱스인 경우
        if len(work_day) == 0:
            answer.append(sum)
            break

    return answer