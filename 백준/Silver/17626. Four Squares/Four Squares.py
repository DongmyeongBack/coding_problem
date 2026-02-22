n = int(input())

dp = [4 for _ in range(50000+1)]
dp_one = []

for i in range(300):
  if i**2 <= 50000:
    dp[i**2] = 1
    dp_one.append(i**2)


for i in dp_one:
  if dp[i] == 1:
    for j in dp_one:
      if dp[j] == 1:
        sum = i + j
        if sum <= 50000:
          dp[sum] = min(2, dp[sum])


for i in dp_one:
  if dp[i] == 1:
    for j in dp_one:
      if dp[j] == 1:
        for k in dp_one:
          sum = i + j + k
          if sum <= 50000:
            dp[sum] = min(3, dp[sum])

print(dp[n])