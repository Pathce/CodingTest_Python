def solution(phone_book):
    phone_book.sort(key = len)
    pmin = len(phone_book[0])
    pmax = len(phone_book[-1])
    for i in range(pmin, pmax):
        pdic = {}
        n = 0
        for j in phone_book:
            if len(j) == i:
                pdic[j] = j
            else:
                if n == 0:
                    n = phone_book.index(j)
                if j[:i] in pdic:
                    return False
        del phone_book[:n]


    answer = True
    return answer