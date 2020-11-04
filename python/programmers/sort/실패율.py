def solution(N, stages):
    answer = []
    failure = dict()
    leng = len(stages)
    for i in range(N):
        if i + 1 in stages:
            cnt = stages.count(i + 1)
            failure[i + 1] = cnt / leng
            leng -= cnt
            stages.remove(i + 1)
        else:
            failure[i + 1] = 0

    failure = sorted(failure.items(), key=lambda x: x[1], reverse=True)

    for i in failure:
        answer.append(i[0])
    return answer