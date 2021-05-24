def solution(clothes):
    c_dict = {}
    for i in clothes:
        if i[1] in c_dict:
            c_dict[i[1]] += 1
        else:
            c_dict[i[1]] = 1
        
    result = 1
    for i in c_dict.keys():
        result += result * c_dict[i]
        
    answer = result - 1
    return answer