def solution(wallet, bill):
    answer = 0
    while True:
        if max(wallet[0], wallet[1]) >= max(bill[0], bill[1]) and min(wallet[0], wallet[1]) >= min(bill[0], bill[1]):
            break
        else:
            if bill[0] >= bill[1]:
                bill[0] = bill[0] // 2
            else:
                bill[1] = bill[1] // 2
            answer += 1
    return answer