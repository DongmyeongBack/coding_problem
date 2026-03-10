import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
answers = []

for _ in range(T):
  # N = 건물의 개수, K = 건설규칙수(엣지개수)
  N, K = map(int, input().split()) 
  orderG = [[] for __ in range(N+1)]
  in_degree = [0 for _ in range(N+1)]
  time = list(map(int, input().split()))
  time = [0] + time
  dp = time[:]
  for __ in range(K):
    strNode, endNode = map(int, input().split())
    orderG[strNode].append(endNode)
    in_degree[endNode] += 1

  target = int(input())
  queue = deque([])

  for i in range(N+1):
    if in_degree[i] == 0:
      queue.append(i)

  while queue:
    now = queue.popleft()
    if now == target:
      break
    for next in orderG[now]:
      in_degree[next] -= 1
      dp[next] = max(dp[next], time[next]+dp[now])
      if in_degree[next] == 0:
        queue.append(next)
    # print(now, dp)
    # print(in_degree)

  answers.append(dp[target])

for answer in answers:
  print(answer)
