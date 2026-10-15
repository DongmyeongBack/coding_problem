def solution(brown, yellow):
    answer = []
    width = brown+yellow
    
    for i in range(int(width**0.5)+1):
        if width%(i+1)==0 and not i == 0:
            is_finish = False
            for j in range(brown):
                if ((brown-4)//2-j-1)*(j+1) == yellow:
                    answer.append((brown-4)//2-j+1)
                    answer.append(j+3)
                    is_finish = True
                    break
            if is_finish: break
    print(answer)
    return sorted(answer, reverse = True)