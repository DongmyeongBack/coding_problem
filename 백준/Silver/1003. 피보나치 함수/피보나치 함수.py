import sys
input = sys.stdin.readline

T = int(input())
answers = []

for _ in range(T):
  N = int(input())
  dp = [[0 for _ in range(N+1)] for __ in range(2)]
  
  for i in range(N+1):
    if i == 0:
      dp[0][0] = 1
    elif i == 1:
      dp[1][1] = 1
    else:
      dp[0][i] = dp[0][i-1] + dp[0][i-2]
      dp[1][i] = dp[1][i-1] + dp[1][i-2]
  answers.append([dp[0][-1], dp[1][-1]])

for answer in answers:
  print(answer[0], answer[1])
