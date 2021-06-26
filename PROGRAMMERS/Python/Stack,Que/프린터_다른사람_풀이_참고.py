def solution(priorities, location):
    answer = 0
    que = ([(i, pri) for i, pri in enumerate(priorities)])
    
    while True:
        cur = que.pop(0)
        if any(cur[1] < q[1] for q in que):
            que.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer