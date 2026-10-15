def solution(k, tangerine):
    answer = 0
    type = {}
    for tar in tangerine:
        if tar in type:
            type[tar] += 1
        else:
            type[tar] = 1
    my_type = type.items()
    my_type = sorted(my_type, key = lambda x: x[1], reverse = True)
    for i in range(k):
        if k <=0:
            break
        k = k-my_type[i][1]
        answer += 1
    return answer