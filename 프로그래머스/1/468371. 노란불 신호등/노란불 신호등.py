def solution(signals):
    answer = -1
    n = len(signals)
    
    max_time = 1
    periods = list()
    for signal in signals:
        periods.append(signal[0] + signal[1] + signal[2])
        max_time = max_time * periods[-1]
    
    time_list = list()
    for i in range(n):
        tmp = 0
        while True:
            if signals[i][0] + periods[i] * tmp > max_time:
                break
            for j in range(signals[i][1]):
                time_list.append(signals[i][0]+ periods[i]*tmp + j +1)
            tmp += 1
            
    time_list.sort()
    for i in range(len(time_list)):
        answer_flag = 1
        for j in range(n):
            if not time_list[i] == time_list[i-j]:
                answer_flag = -1
        if answer_flag == 1:
            answer = time_list[i]
            break
    
    return answer