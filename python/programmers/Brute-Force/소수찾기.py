from itertools import permutations
numbers = "011"

def solution(numbers):
    answer = 0
    made_numbers=[]
    permutated_paper = [i for i in numbers]
    for i,v in enumerate(permutated_paper):
        made_numbers+=map(int, list(map(''.join, permutations(permutated_paper, i+1))))
    made_numbers=set(made_numbers)
    for i in made_numbers:
        if i == 0 or i == 1:
            continue
        decimal = True
        sqrt_num = int(i ** 0.5)
        for j in range(2, sqrt_num + 1):
            if i % j == 0:
                decimal = False
                break
        if decimal == True:
            answer += 1

    return answer


print(solution(numbers))