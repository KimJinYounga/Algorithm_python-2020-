from collections import defaultdict
genres= ["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []

    # defaultdict(int)로 설정하면 value값이 default 0으로 설정됨.
    genre_rank=defaultdict(int)
    play_detail = defaultdict(list)
    for i,v in enumerate(genres):
        genre_rank[v]+=plays[i]
        play_detail[v].append((plays[i], i))


    # value값을 기준으로 내림차순 정렬
    genre_rank=sorted(genre_rank.items(),
                              reverse=True,
                              key=lambda item: item[1])

    for _ in range(len(genre_rank)):
        big = genre_rank.pop(0)[0]
        play_detail[big]=sorted(play_detail[big], reverse=True, key=lambda item:item[0])

        if len(play_detail[big])==1:
            answer.append(play_detail[big][0][1])
        else:
            answer.append(play_detail[big][0][1])
            answer.append(play_detail[big][1][1])

    return answer



print(solution(genres, plays))