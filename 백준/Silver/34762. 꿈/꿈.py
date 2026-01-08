N, K = map(int, input().split())
M = int(input())
goodDreams = list(map(int, input().split()))

canSolve = True
for i in range(M-1):
    if goodDreams[i+1]-goodDreams[i]>1 and goodDreams[i+1]-goodDreams[i]<=K+1:
        canSolve = False
        # print(goodDreams[i])
        break

if not N == goodDreams[-1] and N - goodDreams[-1] < K+1:
    canSolve = False

if canSolve:
    print("YES")
else:
    print("NO")
        