from collections import deque
def solution(order):
    answer = 0
    index = 1
    sub_order = deque()
    for item in order:
        if not len(sub_order) == 0:
            if index >= len(order) and not item == index and not sub_order[-1] == item:
                break
        if item == index:
            index += 1
            answer += 1
        elif not len(sub_order) == 0 and sub_order[-1] == item:
            sub_order.pop()
            answer += 1
        else:
            while True:
                if index == item:
                    index+=1
                    answer+=1
                    break
                elif index >= len(order):
                    break
                sub_order.append(index)
                index += 1
    return answer