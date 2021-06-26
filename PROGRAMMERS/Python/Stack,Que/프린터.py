def solution(priorities, location):
    que = []
    answer = 0
    
    for num in range(9, 0, -1):
        e = 0
        if que:
            a = que[-1]
            for i in range(a, len(priorities)):
                if priorities[i] == num:
                    que.append(i)
                    if i == location:
                        print(1, i)
                        e = 1
                        break
            if e == 1:
                break
            for i in range(0, a):
                if priorities[i] == num:
                    que.append(i)
                    if i == location:
                        print(2, i)
                        break
        else:
            for i in range(len(priorities)):
                if priorities[i] == num:
                    que.append(i)
                    if i == location:
                        print(3, i)
                        break
        
        if num == priorities[location]:
            break
            
    print(que)
            
    answer = len(que)
    
    return answer