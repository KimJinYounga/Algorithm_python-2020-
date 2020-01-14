from collections import defaultdict
genres= ["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []

    # defaultdict(int)로 설정하면 value값이 default 0으로 설정됨.
    genre_rank=defaultdict(int)

    # defaultdict(list)로 설정하면 value값이 리스트 형식으로 설정됨.
    play_detail = defaultdict(list)

    # genre_rank는 각 키에 해당하는 모든 연주횟수를 더함
    # play_detail 객체에 key : 노래장르, value : (plays 리스트값, 인덱스값)들을 묶어서 저장
    # "classic" : [(800,3), (500,0), (150,2)] , ...
    for i,v in enumerate(genres):
        genre_rank[v]+=plays[i]
        play_detail[v].append((plays[i], i))


    # 가장 많이 재생된 장르순으로 정렬
    # value값을 기준으로 내림차순
    genre_rank=sorted(genre_rank.items(),
                              reverse=True,
                              key=lambda item: item[1])

    # 각 장르에 속한 곡들을 내림차순으로 정렬
    for _ in range(len(genre_rank)):
        big = genre_rank.pop(0)[0]
        play_detail[big]=sorted(play_detail[big], reverse=True, key=lambda item:item[0])

        # 제한사항 ==> 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
        if len(play_detail[big])==1:
            answer.append(play_detail[big][0][1])
        else:
            answer.append(play_detail[big][0][1])
            answer.append(play_detail[big][1][1])

    return answer



print(solution(genres, plays))