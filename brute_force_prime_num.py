from itertools import permutations


def permutation(i_list):
    o_list = []
    for i in range(1, len(i_list) + 1):
        per = tuple(permutations(i_list, i))
        for j in range(len(per)):
            o_list.append(int(''.join(per[j])))
    return set(o_list)


def find_prime(i_list):
    print(i_list)
    prime = len(i_list)
    for i in i_list:
        print(i)
        if i < 2:
            prime -= 1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                prime -= 1
                break
    return prime


def solution(numbers):
    new_list = list(numbers)
    return find_prime(list(permutation(new_list)))


numbers = '017'
print(solution(numbers))
i = 701
print(i**0.5)
