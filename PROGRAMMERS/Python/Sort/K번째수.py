def solution(array, commands):
    answer = []
    for com in commands:
        start_num = com[0] - 1
        end_num = com[1]
        select_num = com[2] - 1
        ar = array[start_num:end_num]
        ar.sort()
        answer.append(ar[select_num])
    return answer