from collections import deque

nodeNum = int(input())
linkLen = int(input())


links = [[] for _ in range(nodeNum+1)]

for _ in range(linkLen):
    start, end = map(int, input().split())
    links[start].append(end)
    links[end].append(start)

visited = list(False for _ in range(nodeNum+1))
# 0번 노드는 빼고 생각하자

# links를 통해 bfs실행 visited면 안가기

queue = deque([1])
visited[1] = True

while queue:
    now = queue.popleft()
    for next in links[now]:
        if not visited[next]:
            queue.append(next)
            visited[next] = True
    

count = 0
for isVirus in visited:
    if isVirus:
        count += 1

print(count-1)