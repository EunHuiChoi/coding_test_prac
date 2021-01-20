def solution(answers):
    fir = [1, 2, 3, 4, 5]
    fir *= 2000
    sec = [2, 1, 2, 3, 2, 4, 2, 5]
    sec *= 2000
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    thr *= 2000
    f_c = 0
    s_c = 0
    t_c = 0

    for a, f, s, t in zip(answers, fir, sec, thr):
        if a == f:
            f_c += 1
        if a == s:
            s_c += 1
        if a == t:
            t_c += 1
    answer_dict = {'1': f_c, '2': s_c, '3': t_c}
    answer = [k for k, v in answer_dict.items() if v == max(answer_dict.values())]
    return list(map(int, answer))


# answers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# answers = [1, 3, 2]
answers = [1, 3, 2, 4, 2]
print(solution(answers))
