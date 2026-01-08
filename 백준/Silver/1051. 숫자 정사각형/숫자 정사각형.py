N, M = map(int,input().split())

rect = []
for _ in range(N):
    rect.append(list(input()))


def isSquare(col, row):
    global N
    global M

    maxSide = 0
    for side in range(min(N-col, M-row)):
        if rect[col][row] == rect[col+side][row] and  rect[col][row] == rect[col][row+side] and rect[col][row] == rect[col+side][row+side]:
            maxSide = max(maxSide, side)            
    return maxSide


ans = 0
for i in range(N): 
    for j in range(M):
        ans = max(ans, isSquare(i,j))
ans += 1
print(ans**2)