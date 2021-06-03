num_rooms = [[4],
             [11],
             [2, 4, 2, 6],
             [6, 6, 4, 2],
             [2, 2, 1, 2],
             [4, 4, 5, 3]]

def Research(num_list, current_room, line, target):
    result = []
    line_h = line - current_room[0]
    line_v = line - current_room[1]
    list_v = []

    for v in range(line_v):
        list_h = []
        list_v.append(num_list[current_room[0]][current_room[1]+v])
        if sum(list_v) >= target:
            if sum(list_v) == target:
                result.append(list_v)
            break
        else:
            for h in range(line_h - 1):
                list_h.append(num_list[current_room[0]+1+h][current_room[1]+v])
                if sum(list_v) + sum(list_h) >= target:
                    if sum(list_v) + sum(list_h) == target:
                        list_r = list_v + list_h
                        result.append(list_r)
                    break

    list_h = []
    for h in range(line_h):
        list_v = []
        list_h.append(num_list[current_room[0]+h][current_room[1]])
        if sum(list_h) >= target:
            if sum(list_h) == target:
                result.append(list_h)
            break
        else:
            for v in range(line_v - 1):
                list_v.append(num_list[current_room[0]+h][current_room[1]+1+v])
                if sum(list_h) + sum(list_v) >= target:
                    if sum(list_h) + sum(list_v) == target:
                        list_r = list_h + list_v
                        result.append(list_r)
                    break

    return result


def Solution(num_rooms):
    line = num_rooms[0][0]      # N*N 배열의 N
    target = num_rooms[1][0]    # 목표 숫자
    num_list = num_rooms[2:]    # 1, 2번 라인을 제외한 리스트
    current_room = [0, 0]       # 현재 탐색중인 위치를 표시할 리스트
    answer = []

    for list_v in num_list:
        current_room[1] = 0
        for num in list_v:
            research_result = Research(num_list, current_room, line, target)
            if research_result != [[]]:
                for i in research_result:
                    answer.append(i)
            current_room[1] += 1
        current_room[0] += 1

    return answer

if __name__ == "__main__":
    for result in Solution(num_rooms):
        print(result)