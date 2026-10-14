def solution(n, w, num):
    answer = 0
    is_num_left = True
    if ((num-1)//w + 1) % 2 == 0:
        is_num_left = False
    
    is_top_left = True
    if ((n-1)//w + 1) % 2 == 0:
        is_top_left = False
        
    if is_num_left == is_top_left:
        answer = (n-num)//w+1
    else:
        answer = ((n-num)//(2*w))*2+1
        if w-((n-1)%w)<=(num-1)%w+1:
            answer += 1
    return answer