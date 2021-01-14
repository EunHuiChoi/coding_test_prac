# 장르 별 순서는 해당 장르의 모든 곡의 play의 합

def solution(genres, plays):
    album_dict = {}
    answer = []
    # 인덱스 저장을 위해 enumerate 함수 이용
    new_plays = tuple(enumerate(plays))

    # 장르와 플레이 수 매칭
    a_list = list((zip(genres, new_plays)))

    # 매칭된 값 딕셔너리로 만들기
    for k, v in a_list:
        album_dict.setdefault(k, []).append(v)

    # value 정렬
    for v_list in album_dict.values():
        v_list.sort(key=lambda l: l[-1], reverse=True)

    # value 간의 합 리스트 첫번째 자리로 삽입
    for i in album_dict:
        album_dict[i].insert(0, sum(item[1] for item in album_dict[i]))

    # value 첫번째 값으로 딕셔너리 정렬
    new_dict = dict(sorted(album_dict.items(), key=lambda item: item[1][0], reverse=True))

    # 정렬 완료된 후, 인덱스 리스트에 저장
    for i in new_dict.values():
        del i[0]
        if len(i) > 2:
            del i[2:]
        for j in i:
            answer.append(j[0])
    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))
