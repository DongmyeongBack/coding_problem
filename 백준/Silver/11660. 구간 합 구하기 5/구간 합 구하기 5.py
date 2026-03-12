import sys
input = sys.stdin.readline

N, M = map(int, input().split())

myList = [[0 for _ in range(N+1)]]
for _ in range(N):
  tmp = list(map(int, input().split()))
  tmp = [0] + tmp
  myList.append(tmp)

sumList = [[0 for i in range(N+1)] for _ in range(N+1)]

for i in range(N):
  for j in range(N):
    sumList[i+1][j+1] = sumList[i][j+1] + sumList[i+1][j] - sumList[i][j] + myList[i+1][j+1]

answers = []
for _ in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  answers.append(sumList[x2][y2] - sumList[x2][y1-1] - sumList[x1-1][y2] + sumList[x1-1][y1-1])

for answer in answers:
  print(answer)
