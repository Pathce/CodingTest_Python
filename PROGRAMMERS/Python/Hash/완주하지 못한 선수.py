def solution(participant, completion):
    pa = participant
    co = completion
    pa.sort()
    co.sort()
    co.append("")
    i = 0
    while (pa[i] == co[i]):
        i += 1
    answer = pa[i]

    return answer