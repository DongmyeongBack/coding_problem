#https://www.acmicpc.net/problem/1012
#실패
import sys
sys.setrecursionlimit(100000)

T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
  global bachu
  global dx
  global dy

  land[x][y] = 0

  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if -1<nx<M and -1<ny<N:
      if land[nx][ny] == 1:
        dfs(nx, ny)

  
countList = []
for _ in range(T):
  M, N, numBachu = map(int, input().split())
  land = [[0 for _ in range(N)]for _ in range(M)]
  bachu = []

  for _ in range(numBachu):
    tmpx, tmpy = map(int, input().split())
    bachu.append([tmpx, tmpy])
    land[tmpx][tmpy] = 1

  count = 0
  for i in range(M):
    for j in range(N):
      if land[i][j] == 1:
        count += 1
        dfs(i, j)

  countList.append(count)
  
for ans in countList:
  print(ans)

