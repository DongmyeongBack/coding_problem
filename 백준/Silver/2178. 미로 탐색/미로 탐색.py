from collections import deque
import sys

input = sys.stdin.readline

N,M = map(int, input().split())

maze = []
for _ in range(N):
  mazeRow = list(map(int, input().rstrip()))
  maze.append(mazeRow)

myDeque = deque([(0,0)])

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# print(maze)

while myDeque:
  now = myDeque.popleft()

  if now[0] == N -1 and now[1] == M -1:
    print(maze[now[0]][now[1]])
    break

  for i in range(4):
    nextr = now[0]+dr[i]
    nextc = now[1]+dc[i]
    # print("nextPosition:", nextr, nextc)/
    if -1 < nextr < N and -1 < nextc < M:
      if maze[nextr][nextc] == 1:
        myDeque.append((nextr, nextc))
        maze[nextr][nextc] = maze[now[0]][now[1]] + 1

