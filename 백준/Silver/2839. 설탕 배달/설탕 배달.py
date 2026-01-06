#https://www.acmicpc.net/problem/2839

N = int(input())


def cal():
  fiveKg = N // 5
  lastKg = N % 5

  invalidKg = [1, 2, 4, 7]
  for kg in invalidKg:
    if kg == N:
      print(-1)
      return

  if lastKg == 0:
    print(fiveKg)
  elif lastKg == 1 or lastKg == 3: 
    print(fiveKg+1)
  else:
    print(fiveKg+2)
cal()