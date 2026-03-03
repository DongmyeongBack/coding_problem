import sys
input = sys.stdin.readline

num = list(map(int, input().rstrip()))

dp = [1 for _ in range(len(num))]

possible = True

for i in range(len(dp)):
  # print(i, dp)
  if i == 0:
    if num[i] == 0:
      possible = False
      break
  else:
    # print(10*num[i-1]+num[i])
    if 10 <= 10*num[i-1]+num[i] <= 26:
      if num[i] == 0:
        dp[i] = max(dp[i-2], dp[i])
      else:
        if i == 1:
          # print("2222222")
          dp[i] = 2
        else:
          dp[i] = dp[i-1] + dp[i-2]
    else:
      if num[i] == 0:
        possible = False
        break
      else:
        dp[i] = max(dp[i-1], dp[i])

if possible:
  print(dp[-1]%1000000)
else:
  print(0)