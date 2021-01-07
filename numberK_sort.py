def sort(input_array):
    i = 0
    j = i + 1
    for i in range(len(input_array)):
        position = i
        for j in range(i, len(input_array)):
            if input_array[position] > input_array[j]:
                position = j
        input_array[i], input_array[position] = input_array[position], input_array[i]
    return input_array


def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        z = 1  # array 인덱스 체크 임시 변수
        new_array = list()

        for new in array:
            if (z >= i) & (z <= j):
                new_array.append(new)
            z = z + 1

        sort_array = sort(new_array)
        answer.append(sort_array[k-1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))

