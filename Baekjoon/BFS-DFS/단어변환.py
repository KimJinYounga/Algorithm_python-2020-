# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
# def solution(begin, target, words):
#     if target not in words:
#         return 0
#     answer = 0
#
#     def bfs(begin):
#         nonlocal answer
#         visited = [begin]
#         stacks= [begin]
#         while stacks:
#             n = stacks.pop()
#             if n==target:
#                 return answer
#
#             for v in words:
#                 if sum(1 for a,b in zip(v, n) if a!=b)==1:
#                     if v not in visited:
#                         stacks.append(v)
#                         visited.append(v)
#             answer += 1
#     bfs(begin)
#     return answer
#
#
# print(solution(begin, target, words))





begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

def solution(begin, target, words):
    # 1. 현재 노드에서 갈 수 있는 다른 경로 구하는 함수
    def get_path(current):
        arr = []
        for word in words:
            count = 0
            for i in range(len(current)):
                if current[i] == word[i]: count += 1
            if count == len(current) - 1:
                arr.append(word)
        return arr

    # 2. path에 각 노드 별 변환 될 수 있는 모든 노드 리스트 저장
    def init_path():
        path = {}
        words.append(begin) # 초기값도 추가

        # path 초기화
        for word in words:
            res = get_path(word)
            if word not in path.keys():
                path[word] = res
            else:
                path[word].append(res)
        return path

    def bfs():
        answer = []
        queue = [(begin, [begin])]
        path = init_path()
        print("-----")
        for i in path:
            print(i," : ", path[i])
        print("-----")

        # 3. 첫 단어를 시작으로 BFS로 인접한 노드를 방문합니다.
        while queue:
            current, visited = queue.pop(0)

            # 4. 현재 단어와 target이 같으면 정답에 도달 !
            if current == target:
                answer = visited
                break

            # 인접한 노드를 방문
            for node in path[current]:
                if node not in visited:
                    queue.append((node, visited + [node]))
                    print("queue = ", queue)
        return len(answer) - 1

    # target이 words에 없으면 답을 못 구하니 0 반환
    if target not in words: return 0

    answer = bfs()

    return answer

print(solution(begin,target, words))