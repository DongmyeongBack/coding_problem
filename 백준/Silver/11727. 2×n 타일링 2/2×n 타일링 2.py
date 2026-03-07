import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n)]

for i in range(n):
  if i == 0:
    dp[0] = 1
  elif i == 1:
    dp[1] = 3
  else:
    dp[i] = dp[i-1]+dp[i-2]*2

print(dp[n-1]%10007)