from collections import deque

computerNum = int(input())
edgeNum = int(input())

graph = list([] for _ in range(computerNum + 1))

for i in range(edgeNum):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visited = []

queue = deque([1])
visited = [1]

while queue:
  currentNode = queue.popleft()
  for i in graph[currentNode]:
    if i not in visited:
      queue.append(i)
      visited.append(i)
      
print(len(visited) - 1)