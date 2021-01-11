def solution(clothes):
    cloth_dict = {}
    for k, v in clothes:
        cloth_dict.setdefault(v, []).append(k)
    answer = 1
    for i in cloth_dict.values():
        answer *= len(i) + 1
    return answer - 1


clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(clothes))