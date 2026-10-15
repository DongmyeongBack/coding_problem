def solution(strings, n):
    answer = []
    strings.sort()
    for i in range(ord("a"), ord("z") + 1):
        for string in strings:
            if string[n] == chr(i): answer.append(string)
    return answer