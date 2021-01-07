def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    temp = ''.join(str(i) for i in numbers)
    answer = int(temp)
    return str(answer)


eg_array = [0, 0, 0, 0, 0]
print(solution(eg_array))
