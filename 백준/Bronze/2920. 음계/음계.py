import sys
input = sys.stdin.readline

order = list(map(int, input().split()))

isBreak = False
if order[0] == 1:
  for i in range(1,8):
    if not order[i] == order[i-1]+1:
      print("mixed")
      isBreak = True
      break
  if not isBreak:
    print("ascending")
elif order[0] == 8:
  for i in range(1, 8):
    if not order[i] == order[i-1]-1:
      print("mixed")
      isBreak = True
      break
  if not isBreak:
    print("descending")
else:
  print("mixed")