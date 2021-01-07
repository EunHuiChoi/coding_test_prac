def solution(citations):
    answer = 0
    for i in range(0, len(citations)+1):
        k = 0
        for c in citations:
            if c >= i:
                k += 1
                if i == k:
                    answer = k
    return answer


eg_array = [3, 0, 6, 1, 5]
print(solution(eg_array))
