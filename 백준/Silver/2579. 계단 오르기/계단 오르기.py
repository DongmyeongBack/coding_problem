import sys
input = sys.stdin.readline

N = int(input())
scores = []

for _ in range(N):
  scores.append(int(input()))

dp = scores[:]

for i in range(N-1):
  if i+2 <= N-1:
    dp[i+2] = max(dp[i+2], dp[i]+scores[i+2])
  if i+3 <= N-1:
    dp[i+3] = max(dp[i+3], dp[i]+scores[i+1]+scores[i+3])
  if i+1 == N-1:
    dp[i+1] = max(dp[i+1], dp[i]+scores[i+1])

print(dp[N-1])