heights=[1,5,3,6,7,6,5]

def solution(heights):
    answer = []
    for i in range(1,len(heights)):
        # for loop 거꾸로 출력 : -1옵션(range 메소드의 3번째 인자)
        # i, i-1, i-2, ... ,0
        for j in range(i, -1, -1):
            if heights[j] > heights[i]:
                answer.append(j+1)
                break
            if j==0:
                answer.append(0)

    return [0]+answer

print(solution(heights))