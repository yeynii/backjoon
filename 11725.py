from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = list([] for _ in range(n+1))

for i in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

rootNode = list([] for _ in range(n+1))
visited = [False] * (n + 1)
queue = deque([1])

while queue:
  current = queue.popleft()
  visited[current] = True
  for v in graph[current]:
    if not visited[v]:
      queue.append(v)
      rootNode[v] = current
      
for r in rootNode[2:]:
  print(r)