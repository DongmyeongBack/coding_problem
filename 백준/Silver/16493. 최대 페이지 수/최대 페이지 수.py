import sys
input = sys.stdin.readline

# 남은기간 N일, 챕터수 M개
N, M = map(int, input().split())

dp = [0 for _ in range(N+1)]

for _ in range(M):
  numDays, numPages = map(int, input().split())

  for day in range(N, numDays-1, -1):
    dp[day] = max(dp[day], dp[day-numDays]+numPages)

print(dp[N])