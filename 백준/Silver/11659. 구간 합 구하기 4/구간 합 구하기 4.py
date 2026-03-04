import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numList = list(map(int, input().split()))
sumList = []

sum = 0
for num in numList:
  sum += num
  sumList.append(sum)

answers = []
for _ in range(M):
  strP, endP = map(int, input().split())
  strP -= 1
  endP -= 1
  
  if strP == endP:
    answers.append(numList[strP])
  elif strP == 0:
    answers.append(sumList[endP])
  else:
    answers.append(sumList[endP]-sumList[strP-1])

for ans in answers:
  print(ans)

