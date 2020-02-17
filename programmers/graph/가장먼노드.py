from collections import defaultdict

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, edge):

    answer = 0
    depth = {i:0 for i in range(1, n+1)}
    visited = {i:False for i in range(1, n+1)}
    adj = defaultdict(list)

    # adj2['one'] = '1'
    for i in edge:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])
    qlist = adj[1]
    floor = 1
    while qlist:
        len_adj = len(qlist)
        for i in range(len_adj):
            node = qlist.pop(0)
            if visited[node] ==False:
                visited[node] =True
                depth[node] = floor
                qlist+=adj[node]
        floor+=1
    del depth[1]
    maxValue = max(depth.values())
    answer = list(depth.values()).count(maxValue)
    # for i in depth.values():
    #     if i == maxValue:
    #         answer+=1
    return answer

print(solution(n, edge))
