import sys
input = sys.stdin.readline

T = int(input())

ans = []
for _ in range(T):
  N = int(input())

  if N == 1:
    ans.append(1)
  elif N == 2:
    ans.append(2)
  elif N == 3:
    ans.append(4)
  else:
    dp = [0 for _ in range(N+1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, N+1, 1):
      dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    # print(dp, N)
    ans.append(dp[N])

for num in ans:
  print(num)
