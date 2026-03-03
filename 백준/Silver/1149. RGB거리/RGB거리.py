import sys
input = sys.stdin.readline

N = int(input())
data = []

for _ in range(N):
  data.append(list(map(int, input().split())))

dp = [data[0][:]]

for i in range(N-1):
  # print(dp)
  dp.append([min(dp[i][1]+data[i+1][0], dp[i][2]+data[i+1][0]),min(dp[i][0]+data[i+1][1], dp[i][2]+data[i+1][1]),min(dp[i][0]+data[i+1][2], dp[i][1]+data[i+1][2])])

print(min(dp[-1][0], dp[-1][1], dp[-1][2]))