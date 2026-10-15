from collections import deque

def solution(s):
    answer = 0
    
    stack = deque()
    
    for string in s:
        if len(stack) == 0:
            stack.append(string)
        elif string == stack[-1]:
            stack.pop()
        else:
            stack.append(string)
    if len(stack) == 0:
        answer = 1
    return answer