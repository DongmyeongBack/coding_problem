from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

paper = []

def BFS(row, col):
  result = 1
  myDeque = deque([(row,col)])
  paper[row][col] = 0
  dr = [0, 1, 0, -1]
  dc = [1, 0, -1, 0]

  while myDeque:
    now = myDeque.popleft()
    for i in range(4):
      nextr = now[0]+dr[i]
      nextc = now[1]+dc[i]
      if -1 < nextr < N and -1 < nextc < M:
        if paper[nextr][nextc] == 1:
          myDeque.append((nextr, nextc))
          paper[nextr][nextc] = 0
          result += 1
          # print(result, nextr, nextc)

  return result
  

for _ in range(N):
  paperRow = list(map(int, input().split()))
  paper.append(paperRow)

numDraw = 0
numArea = 0
for r in range(N):
  for c in range(M):
    if paper[r][c] == 1:
      numDraw += 1
      area = BFS(r,c)
      numArea = max(area, numArea)
      
print(numDraw)
print(numArea)