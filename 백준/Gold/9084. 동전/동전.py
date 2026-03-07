import sys
input = sys.stdin.readline

T = int(input())

answers = []
for _ in range(T):
  N = int(input())
  coins = list(map(int, input().split()))
  amount = int(input())

  dp = [0 for __ in range(amount+1)]
  dp[0] = 1

  for coin in coins:
    for i in range(amount + 1):
      if i >= coin:
        dp[i] += dp[i-coin]
        
  answers.append(dp[amount])

for answer in answers:
  print(answer)