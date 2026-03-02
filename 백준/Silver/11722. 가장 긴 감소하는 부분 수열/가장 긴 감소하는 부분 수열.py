import sys
input = sys.stdin.readline

A = int(input())
N = list(map(int, input().split()))

dp = [1 for _ in range(len(N)+1)]

for i in range(len(N)):
  nmax = 0
  for j in range(i, -1, -1):
    if N[i] < N[j]:
      nmax = max(nmax, dp[j])
  dp[i] = max(dp[i], nmax+1)

answer = 0
for num in dp:
  answer = max(num, answer)

print(answer)