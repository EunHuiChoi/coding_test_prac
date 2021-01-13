def solution(phone_book):
    phone_book.sort(key=str)
    new_list = []
    temp_list = []
    for i in phone_book:
        new_list.append(list(i))
    for j in range(len(new_list)-1):
        check_tuple = tuple(zip(new_list[j], new_list[j + 1]))
        temp_list.clear()
        for ct in check_tuple:
            if ct[0] == ct[1]:
                temp_list.append(False)
            else:
                temp_list.append(True)
        if not any(temp_list):
            return False
    return True


phone_book = ['119', '97674223', '1195524421']    # False
# phone_book = ['123', '456', '789']  # True
# phone_book = ["113", "44", "4544"]    # True
print(solution(phone_book))
