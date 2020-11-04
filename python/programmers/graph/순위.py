n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

def solution(n, results):
    answer = 0
    len_results = len(results)
    rank_arr = [[0 for i in range(n)] for i in range(n)]

    for i in range(len_results):
        a, b = results[i]
        rank_arr[a-1][b-1] = 1
        rank_arr[b-1][a-1] = -1

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j==k:
                    rank_arr[j][k] = 1
                if rank_arr[j][k] == 0 and rank_arr[j][i] == rank_arr[i][k]:
                    rank_arr[j][k] = rank_arr[i][k]

    for i in rank_arr:
        if 0 not in i:
            answer+=1

    return answer

print(solution(n, results))