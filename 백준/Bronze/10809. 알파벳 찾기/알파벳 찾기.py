import sys
input = sys.stdin.readline

word = input()
alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

answers = [-1 for _ in range(len(alphabet))]

for i in range(len(answers)):
  for j in range(len(word)):
    if word[j] == alphabet[i]:
      answers[i] = j
      break

for answer in answers:
  print(answer, end = ' ')