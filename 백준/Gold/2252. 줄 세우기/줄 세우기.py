import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
adjList = [[] for _ in range(N+1)] 
visited = [False for _ in range(N+1)]
queue = deque([])

for _ in range(M):
  high, low = map(int, input().split())
  adjList[high].append(low)
  
def DFS(startI):
  visited[startI] = True

  for nextI in adjList[startI]:
    if not visited[nextI]:
      DFS(nextI)

  queue.append(startI)
  return

for i in range(N):
  if not visited[i+1]:
    DFS(i+1)

while queue:
  answer = queue.pop()
  print(answer, end = " ")
