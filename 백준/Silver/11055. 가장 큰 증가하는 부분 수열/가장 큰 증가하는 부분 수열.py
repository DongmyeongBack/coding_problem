import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = A[0]
for now in range(N):
  for search in range(now):
    if A[search] < A[now]:
      dp[now] = max(dp[now], dp[search]+A[now])
    else:
      dp[now] = max(dp[now], A[now])
  # print(dp)

print(max(dp))