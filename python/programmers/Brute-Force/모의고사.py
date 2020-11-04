answers=[1,2,3,4,5]
supo_answers=[[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]

def solution(answers):
    answer = []
    score = [0 for i in range(3)]

    for i in range(3):
        temp = 0
        for j in range(len(answers)):
            if answers[j] == supo_answers[i][temp]:
                score[i]+=1
            temp+=1
            if temp == len(supo_answers[i]):
                temp = 0

    max_score = max(score)
    for i,v in enumerate(score):
        if max_score == v:
            answer.append(i+1)

    return answer

print(solution(answers))