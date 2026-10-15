def solution(board):
    answer = 0
    if len(board) < 2 or len(board[0]) < 2:
        answer = 1
    for r in range(1, len(board)):
        for c in range(1, len(board[0])):
            if board[r][c] == 1:
                board[r][c] = min(board[r-1][c-1], board[r][c-1], board[r-1][c])+1
                if  board[r][c] > answer: answer = board[r][c]
                
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(answer)
    return answer**2