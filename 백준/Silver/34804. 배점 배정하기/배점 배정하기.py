import sys
N, M = map(int, sys.stdin.readline().rstrip().split())

students = []
scores = []

for _ in range(N):
    student = list(map(int, sys.stdin.readline().rstrip().split()))
    score = 0
    if student[0] == 0:
        pass
    else:
        for i in range(len(student)-1):
            score += 2**(student[i+1]-1)
    students.append(student)
    scores.append(score)

scores.sort()

isSame = False
for i in range(len(scores)-1):
    if scores[i] == scores[i+1]:
        isSame = True
        break
if isSame:
    print(-1)
else:
    for i in range(M):
        print(2**(i), end=" ")
